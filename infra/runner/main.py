import logging
import pickle
from random import randint, seed

import pandas as pd

from lyra_observer import LyraMetrics
from lyra_tracker import LyraTrackerManager

MODEL_BINARY_PATH = "/service/model"
DATA_TMP_PATH = "/data"


# Логгеры данных
def tracker_count_features_frame(model, X: pd.DataFrame) -> int:
    """ Кол-во фиче в датасете """
    return len(X.columns)


def tracker_len_frame(model, X: pd.DataFrame) -> int:
    """ Кол-во наблюдений датасета """
    return len(X)


def tracker_count_classes(model, X: pd.DataFrame) -> int:
    """ Кол-во классов в предсказаннии """
    y = model.model.predict(X)
    return len(set(y))


def format_x_data(raw_data: pd.DataFrame) -> pd.DataFrame:
    """ Форматируем вх. датасет"""
    raw_data = raw_data.groupby(["client_id", "report_date"]).sum()
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


def init(m: LyraTrackerManager):
    """ инициализирющий метод """
    try:
        X = pd.read_csv(f"{DATA_TMP_PATH}/X.csv")
        # LYRA_METRICS_HOST — env переменная для хоста, ее необходимо установить, чтобы данные пушились в нужное место
        metric = LyraMetrics(host="", model_name=m.name, model_version=m.version)

        for k in model.trackers:
            tracker = model.trackers[k]

            x = format_x_data(X)
            tracking_metric = tracker(model=m, X=x)

            #  в качестве MVP кладем в прометеус ВСЕ виды данных
            metric.counter(metric_name=k, value=tracking_metric)
            metric.set(metric_name=k, value=tracking_metric)
            metric.observe(metric_name=k, value=tracking_metric)
    except Exception as err:
        logging.error(f"error to init lyra runner {err}")


if __name__ == "__main__":
    with open(MODEL_BINARY_PATH, "rb") as f:
        model: LyraTrackerManager = pickle.load(f)

    # эмулируем real-time
    while True:
        init(model)
