from dataclasses import dataclass
import time

from prometheus_client import start_http_server, Gauge

import logging
from pyrsmi import rocml

logger = logging.getLogger(__name__)


import platform
HOSTNAME = platform.node()

LABEL_GPU = "gpu"
LABEL_MODEL_NAME = "modelName"
LABEL_HOSTNAME = "Hostname"
LABELS = [LABEL_GPU, LABEL_MODEL_NAME, LABEL_HOSTNAME]

def _get_common_labels(gpu: str, model_name: str):
    """
    Returns a dict of the common labels for metric
    """
    res = {}
    res[LABEL_GPU] = gpu
    res[LABEL_MODEL_NAME] = model_name
    res[LABEL_HOSTNAME] = HOSTNAME
    return res


class GPUMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """
    @dataclass
    class Config:
        port: int
        polling_interval_seconds: int

    def __init__(self, config: Config):
        self.config = config

        rocml.smi_initialize()
        ngpus = rocml.smi_get_device_count()
        self.dev_list = list(range(ngpus))

        # Define Prometheus metrics to collect
        self.gpu_utils = [None] * len(self.dev_list)
        self.gpu_mem_utils = [None] * len(self.dev_list)

        # These names are mimicing dcgm-exporter DCGM_FI_DEV_GPU_UTIL and DCGM_FI_DEV_MEM_COPY_UTIL
        GPU_UTIL_METRIC_NAME = "ROCM_SMI_DEV_GPU_UTIL"
        GPU_MEM_UTIL_METRIC_NAME = "ROCM_SMI_DEV_MEM_UTIL"
        self.gpu_util = Gauge(GPU_UTIL_METRIC_NAME, "GPU utilization (in %).", LABELS)
        self.gpu_mem_util = Gauge(GPU_MEM_UTIL_METRIC_NAME, "GPU memory utilization (in %).", LABELS)

    def run_metrics_loop(self):
        """Metrics fetching loop"""
        start_http_server(self.config.port)
        while True:
            logger.info(f"Fetching metrics ...")
            self.fetch()
            time.sleep(self.config.polling_interval_seconds)

    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics.
        """
        for _, dev in enumerate(self.dev_list):
            dev_name = rocml.smi_get_device_name(dev)

            util = rocml.smi_get_device_utilization(dev)
            labels = _get_common_labels(dev, dev_name)
            self.gpu_util.labels(**labels).set(util)
            
            mem_used = rocml.smi_get_device_memory_used(dev)
            mem_total = rocml.smi_get_device_memory_total(dev)
            mem_ratio = mem_used / mem_total
            self.gpu_mem_util.labels(**labels).set(mem_ratio)


import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Parse command line arguments for port and polling interval.')

    parser.add_argument('--port', type=int, default=9001, help='Port number to use.')
    parser.add_argument('--polling-interval-seconds', type=int, default=5, help='Polling interval in seconds.')

    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()

    app_metrics = GPUMetrics(
        GPUMetrics.Config(
            port=args.port,
            polling_interval_seconds=args.polling_interval_seconds
        )
    )
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()
