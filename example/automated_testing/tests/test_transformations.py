import pytest

from pyspark.sql import SparkSession
from pyspark.testing.utils import assertDataFrameEqual

from src.transformations import (
    filter_valid_records,
    aggregate_weather,
)


@pytest.fixture(scope="session")
def spark():
    session = (
        SparkSession.builder
        .master("local[2]")
        .appName("pytest")
        .config("spark.ui.enabled", "false")
        .getOrCreate()
    )

    yield session

    session.stop()


def test_filter_valid_records(spark):
    df = spark.createDataFrame(
        [
            ("Toronto", 10.0),
            ("Ottawa", None),
            ("Vancouver", 15.0),
        ],
        ["city", "temperature"],
    )

    expected = spark.createDataFrame(
        [
            ("Toronto", 10.0),
            ("Vancouver", 15.0),
        ],
        ["city", "temperature"],
    )

    actual = filter_valid_records(df)

    assertDataFrameEqual(actual, expected)


def test_aggregate_weather(spark):
    df = spark.createDataFrame(
        [
            ("Toronto", 10.0),
            ("Toronto", 20.0),
            ("Ottawa", 5.0),
        ],
        ["city", "temperature"],
    )

    expected = spark.createDataFrame(
        [
            ("Toronto", 15.0),
            ("Ottawa", 5.0),
        ],
        ["city", "avg_temperature"],
    )

    actual = aggregate_weather(df)

    assertDataFrameEqual(actual, expected)