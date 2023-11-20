import pytest
import os
from db_connect_test import FlexEnv

# The following will check to see if this is running in the Databricks environment.
# If it is, then we will use the Databricks Spark environment.
# If it is not, then we will use a DatabricksSession through Databricks-connect.
if "DATABRICKS_RUNTIME_VERSION" not in os.environ:
    pytest_plugins = ["spark.db_connect"]
else:
    pytest_plugins = ["spark.db_spark"]


@pytest.fixture(scope="function")
def flex_env(spark_env):
    yield FlexEnv(spark_env)
