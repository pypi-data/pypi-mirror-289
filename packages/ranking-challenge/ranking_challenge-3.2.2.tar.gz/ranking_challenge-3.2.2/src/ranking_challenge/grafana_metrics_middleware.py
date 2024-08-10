import os
import time
import warnings
import requests
import logging
from prometheus_client import CollectorRegistry, Gauge
from prometheus_client.openmetrics.exposition import generate_latest
from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware

# Configure logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

class GrafanaMetricsMiddleware(BaseHTTPMiddleware):
    def __init__(
        self,
        app,
        team_id: str,
        push_interval: int = 15,
        *args,
        **kwargs
    ):
        super().__init__(app, *args, **kwargs)
        self.team_id = team_id
        self.push_interval = push_interval
        self.last_push = time.time()
        self.registry = CollectorRegistry()

        logger.info(f"Initializing GrafanaMetricsMiddleware with team_id: {team_id}, push_interval: {push_interval}")

        # Grafana Cloud configuration
        self.grafana_url = os.getenv('GRAFANA_PUSH_URL')
        self.grafana_username = os.getenv('GRAFANA_USERNAME')
        self.grafana_password = os.getenv('GRAFANA_PASSWORD')

        self.grafana_configured = all([self.grafana_url, self.grafana_username, self.grafana_password])
        
        if self.grafana_configured:
            logger.info("Grafana Cloud credentials configured successfully")
        else:
            logger.warning("Grafana Cloud credentials not fully configured. Metrics will not be pushed to Grafana.")

        # Custom metrics
        self.custom_metrics = {}

    async def dispatch(self, request: Request, call_next):
        logger.debug("Dispatching request")
        response = await call_next(request)

        # Check if it's time to push metrics and if Grafana is configured
        if self.grafana_configured and (time.time() - self.last_push > self.push_interval):
            logger.info("Push interval reached, attempting to push metrics")
            self.push_metrics()
            self.last_push = time.time()

        return response

    def push_metrics(self):
        if self.grafana_configured:
            try:
                logger.debug("Generating metrics data")
                metrics_data = generate_latest(self.registry)
                logger.info(f"Pushing metrics to Grafana: {self.grafana_url}")
                response = requests.post(
                    self.grafana_url,
                    data=metrics_data,
                    auth=(self.grafana_username, self.grafana_password),
                    headers={'Content-Type': 'application/x-protobuf'},
                    timeout=10
                )
                if response.status_code == 204:
                    logger.info("Successfully pushed metrics to Grafana")
                else:
                    logger.warning(f"Failed to push metrics to Grafana. Status code: {response.status_code}")
            except Exception as e:
                logger.error(f"Failed to push metrics to Grafana: {str(e)}", exc_info=True)

    def add_custom_metric(self, metric_name: str, value: float, description: str = "", labels: dict = None):
        logger.debug(f"Adding custom metric: {metric_name}, value: {value}, description: {description}, labels: {labels}")
        
        if labels is None:
            labels = {}
        
        # Always include team_id in labels
        labels['team_id'] = self.team_id

        # Add instance_id to labels if provided in environment
        instance_id = os.getenv('ECS_TASK_ID')
        if instance_id:
            labels['instance_id'] = instance_id
            logger.debug(f"Added instance_id to labels: {instance_id}")

        metric_key = (metric_name, tuple(sorted(labels.items())))
        
        if metric_key not in self.custom_metrics:
            logger.info(f"Creating new Gauge for metric: {metric_name}")
            self.custom_metrics[metric_key] = Gauge(
                metric_name,
                description,
                labelnames=list(labels.keys()),
                registry=self.registry
            )
        
        self.custom_metrics[metric_key].labels(**labels).set(value)
        logger.debug(f"Set value for metric {metric_name}: {value}")

        # If Grafana is not configured, log the metric locally
        if not self.grafana_configured:
            labels_str = ', '.join(f"{k}={v}" for k, v in labels.items())
            logger.info(f"Local metric (not pushed to Grafana): {metric_name}{{{labels_str}}} = {value}")

logger.info("GrafanaMetricsMiddleware module loaded")