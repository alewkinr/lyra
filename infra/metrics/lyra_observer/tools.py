import os
from typing import Optional

from .consts import LyraMetricsConsts


def is_host_defined(host: str = None) -> bool:
    """ Определяем установлен ли хост"""
    _env_host = os.getenv(f"{LyraMetricsConsts.METRICS_HOST_ENV.value}")
    _is_env_set = True if _env_host != "" and _env_host is not None else False

    _is_set_param = True if host != "" and host is not None else False

    return _is_env_set or _is_set_param


def get_host(host: str = None) -> str:
    """ Определяем установлен ли хост"""
    _is_set_param = True if host != "" and host is not None else False
    if _is_set_param:
        return host

    _env_host = os.getenv(f"{LyraMetricsConsts.METRICS_HOST_ENV.value}")
    _is_env_set = True if _env_host != "" and _env_host is not None else False
    if _is_env_set:
        return _env_host

    raise ValueError(f"error to get host for metrics")


def get_namespace() -> Optional[str]:
    """ Определяем неймспейс для модели """
    _ns = os.getenv(f"{LyraMetricsConsts.NAMESPACE.value}")
    if _ns != "" and _ns is not None:
        return _ns
    return None
