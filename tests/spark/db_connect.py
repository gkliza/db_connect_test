import os
import pytest

# Use the Databricks SDK's Config class:
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config

@pytest.fixture(scope="session")
def spark_env():
    config = Config(
        host=os.environ.get('DB_HOST'),
        token=os.environ.get('DB_TOKEN'),
        cluster_id=os.environ.get('DB_CLUSTER_ID')
    )

    spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()
    return spark
