from typing import Any, Callable, Dict, Optional

import pandas as pd


class LyraTrackerManager:
    """ Трекер для метрик """

    _model: Any = None
    _model_name: str = None
    _model_version: str = None
    #  todo: доработать тип трэкера, чтобы ML специалист создавал именно их
    _trackers: Dict[str, Callable] = None

    def __init__(
        self,
        model: Any,
        name: str,
        ops: Dict[str, Callable],
        version: str = "undefined",
    ):
        """ Сохраняем модель в структуру """
        self._model = model
        self._model_name = name
        self._model_version = version

        _ops: Dict[str, Callable] = {}
        for k, v in ops:
            _ops[k] = v

        self._trackers = _ops

    @property
    def name(self):
        """ Геттер для названия """
        return self._model_name

    @property
    def model(self):
        """ Геттер для модели """
        return self._model

    @property
    def version(self):
        return self._model_version

    @property
    def trackers(self) -> Optional[Dict[str, Callable]]:
        """
        Запускаем трекеры
        Идея очень простая: мы даем пачку методов, которые будем запускать из экзекьютора
        а ответ будем обрабатывать, как хочется

        По трекерам можно итерироваться и исполнять
        """
        return self._trackers
