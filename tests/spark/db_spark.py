import os
import pytest

# Use the Databricks SDK's Config class:
from pyspark.sql import SparkSession

@pytest.fixture(scope="session")
def spark_env():
    spark = SparkSession.builder \
        .appName('integrity-tests') \
        .getOrCreate()

    return spark