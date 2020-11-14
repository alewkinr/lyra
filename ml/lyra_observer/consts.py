from enum import Enum


class LyraMetricsConsts(Enum):
    """ Перечисление констант пакета для сбора метрик """

    METRICS_HOST_ENV = "LYRA_METRICS_HOST"
    PUSH_GATEWAY_HOST_DEFAULT = "localhost:9091"
    NAMESPACE = "LYRA_NAMESPACE"

    LABEL_MODEL_NAME = "model_name"
    LABEL_MODEL_VERSION = "model_version"
    LABEL_METRIC_NAME = "metric_name"

    JOB_PREFIX = "lyra_metrics"
