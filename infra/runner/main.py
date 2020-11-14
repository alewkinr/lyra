import logging
import os
import pickle
from random import randint, seed

import pandas as pd

from .lyra_observer import LyraMetrics
from .lyra_tracker import LyraTrackerManager

MODEL_BINARY_PATH = "/service/model"
DATA_TMP_PATH = "/data"


def format_x_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """ Форматируем вх. датасет"""
    raw_data.drop("Unnamed: 0", axis=1, inplace=True)
    seed(1)
    left = randint(0, 2999)
    right = randint(0, 2999)
    if left > right:
        return raw_data[right:left]

    if left < right:
        return raw_data[left:right]

    if left == right:
        return raw_data[left - 1 : right]


def init():
    """ инициализирющий метод """
    try:
        model: LyraTrackerManager = pickle.load(open(MODEL_BINARY_PATH, "rb"))
        X = pd.read_csv(f"{DATA_TMP_PATH}/X.csv")
        # LYRA_METRICS_HOST — env переменная для хоста, ее необходимо установить, чтобы данные пушились в нужное место
        metric = LyraMetrics(
            host="", model_name=model.name, model_version=model.version
        )

        for k, tracker in model.trackers:
            x = format_x_data(X)
            tracking_metric = tracker(model=model, X=x)

            #  в качестве MVP кладем в прометеус ВСЕ виды данных
            metric.counter(metric_name=k, value=tracking_metric)
            metric.set(metric_name=k, value=tracking_metric)
            metric.observe(metric_name=k, value=tracking_metric)

    except Exception as err:
        logging.error(f"error to init lyra runner")
        os.exit(1)


if __name__ == "__main__":
    init()
