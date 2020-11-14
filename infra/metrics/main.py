import pandas as pd

from lyra_observer import LyraMetrics

DATA_PATH = "./data/data.csv"
PROM_PUSH_GATEWAY = "host.docker.internal:9091"


metric = LyraMetrics(PROM_PUSH_GATEWAY, "test_model", "v1")


def main():
    # load sample dataset
    df = pd.read_csv(DATA_PATH)

    #  Итерируемся по DF, чтобы протестировать отправку метрик
    for i, r in df.iterrows():
        metric.set(metric_name="index", value=i)


if __name__ == "__main__":
    main()
