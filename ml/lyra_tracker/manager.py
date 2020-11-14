from typing import Any, Callable, List


class LyraTrackerManager:
    """ Трекер для метрик """

    _model: Any = None
    _model_name: str = None
    _model_version: str = None
    _trackers: List[Callable] = None

    def __init__(
        self,
        model: Any,
        name: str,
        ops: List[Callable],
        version: str = "undefined",
    ):
        """ Сохраняем модель в структуру """
        self._model = model
        self._model_name = name
        self._model_version = version

        _ops = []
        for o in ops:
            if o is not None:
                _ops.append(o)

        self._trackers = _ops

    @property
    def name(self):
        """ Геттер для названия """
        return self._model_name

    @property
    def version(self):
        return self._model_version

    @property
    def trackers(self):
        """
        Запускаем трекеры
        Идея очень простая: мы даем пачку методов, которые будем запускать из экзекьютора
        а ответ будем обрабатывать, как хочется

        По трекерам можно итерироваться и исполнять
        """
        return self._trackers
