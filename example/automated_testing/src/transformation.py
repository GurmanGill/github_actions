from pyspark.sql import DataFrame
from pyspark.sql import functions as F


def filter_valid_records(df: DataFrame) -> DataFrame:
    return df.filter(
        F.col("temperature").isNotNull()
    )


def aggregate_weather(df: DataFrame) -> DataFrame:
    return df.groupBy("city").agg(
        F.avg("temperature").alias("avg_temperature")
    )