from typing import Any, Optional

from prometheus_client import (CollectorRegistry, Counter, Gauge, Histogram,
                               push_to_gateway)

from .consts import LyraMetricsConsts
from .tools import get_host, get_namespace, is_host_defined


class LyraMetrics:
    """ Стандартный класс для отправки метрик в prometheus gateway """

    pushgateway_host: str = LyraMetricsConsts.PUSH_GATEWAY_HOST_DEFAULT.value
    model_name: str = None
    model_version: str = None
    _metrics_registry: CollectorRegistry = None
    _metrics_counter: Counter = None
    _metrics_gauge: Gauge = None
    _metrics_histogram: Histogram = None

    def __init__(self, host: str, model_name: str, model_version: str = "undefined"):
        if not isinstance(host, str):
            raise ValueError(f"push gateway host isn't string a value")

        if not is_host_defined(host):
            raise ValueError(
                f"lyra metrics host is not defined, set {LyraMetricsConsts.METRICS_HOST_ENV.value} variable"
            )
        if not model_name or model_name == "" or model_name is None:
            raise ValueError(f"lyra metrics model name is not set")

        self.pushgateway_host = get_host(host)
        self._metrics_registry = CollectorRegistry()
        self.model_name = model_name
        self.model_version = model_version

        if get_namespace() is not None:
            ns = get_namespace()

        self._metrics_counter = Counter(
            name="lyra_metrics_counter",
            documentation="A counter is a cumulative metric that represents a single monotonically increasing counter whose value can only increase or be reset to zero on restart. For example, you can use a counter to represent the number of requests served, tasks completed, or errors. Do not use a counter to expose a value that can decrease. For example, do not use a counter for the number of currently running processes; instead use a gauge",
            namespace=(get_namespace() if get_namespace() is not None else ""),
            labelnames=[
                LyraMetricsConsts.LABEL_MODEL_NAME.value,
                LyraMetricsConsts.LABEL_MODEL_VERSION.value,
                LyraMetricsConsts.LABEL_METRIC_NAME.value,
            ],
            registry=self._metrics_registry,
        )

        self._metrics_gauge = Gauge(
            name="lyra_metrics_gauge",
            documentation="A gauge is a metric that represents a single numerical value that can arbitrarily go up and down. Gauges are typically used for measured values like temperatures or current memory usage, but also counts that can go up and down, like the number of concurrent requests",
            namespace=(get_namespace() if get_namespace() is not None else ""),
            labelnames=[
                LyraMetricsConsts.LABEL_MODEL_NAME.value,
                LyraMetricsConsts.LABEL_MODEL_VERSION.value,
                LyraMetricsConsts.LABEL_METRIC_NAME.value,
            ],
            registry=self._metrics_registry,
        )

        self._metrics_histogram = Histogram(
            name="lyra_metrics_histogram",
            documentation="A histogram samples observations (usually things like request durations or response sizes) and counts them in configurable buckets. It also provides a sum of all observed values",
            namespace=(get_namespace() if get_namespace() is not None else ""),
            labelnames=[
                LyraMetricsConsts.LABEL_MODEL_NAME.value,
                LyraMetricsConsts.LABEL_MODEL_VERSION.value,
                LyraMetricsConsts.LABEL_METRIC_NAME.value,
            ],
            registry=self._metrics_registry,
        )

    @property
    def registry(self) -> Optional[CollectorRegistry]:
        """ Геттер для реджистри """
        return self._metrics_registry

    def counter(self, metric_name: str, value: Any):
        """ Увеличиваем инкремент метрики """
        self._metrics_counter.labels(
            metric_name=metric_name,
            model_name=self.model_name,
            model_version=self.model_version,
        ).inc(value)
        push_to_gateway(
            self.pushgateway_host,
            job=f"{LyraMetricsConsts.JOB_PREFIX.value}_counter",
            registry=self._metrics_registry,
        )
        pass

    def set(self, metric_name: str, value: Any):
        """ Устанавливаем значение для калибра """
        self._metrics_gauge.labels(
            metric_name=metric_name,
            model_name=self.model_name,
            model_version=self.model_version,
        ).set(int(value))
        push_to_gateway(
            self.pushgateway_host,
            job=f"{LyraMetricsConsts.JOB_PREFIX.value}_gauge",
            registry=self._metrics_registry,
        )
        pass

    def observe(self, metric_name: str, value: Any):
        """ Устанавливаем значение для гистограммы """
        self._metrics_histogram.labels(
            metric_name=metric_name,
            model_name=self.model_name,
            model_version=self.model_version,
        ).observe(value)
        push_to_gateway(
            self.pushgateway_host,
            job=f"{LyraMetricsConsts.JOB_PREFIX.value}_histogram",
            registry=self._metrics_registry,
        )
        pass
