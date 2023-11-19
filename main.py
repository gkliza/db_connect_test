import os
import pyspark

# Use the Databricks SDK's Config class:
from databricks.connect import DatabricksSession
from databricks.sdk.core import Config
from pyspark.sql.functions import lit

config = Config(
    host=os.environ.get('DB_HOST'),
    token=os.environ.get('DB_TOKEN'),
    cluster_id=os.environ.get('DB_CLUSTER_ID')
)

spark = DatabricksSession.builder.sdkConfig(config).getOrCreate()

df = spark.read.table('lmi_dev_raw.stats_can_pid.pid_14100017')
df = df.withColumn('pid', lit('14100017'))

df.show(10)


"""Spark session

Possibilities:
1. This is being run in a Databricks notebook and the Spark environment is already set up
2. This is being run locally and the Spark is provided through Databricks-connect
3. This is being run locally and the Spark is provided through a local Spark installation

If we are in a Databricks notebook:
- if "DATABRICKS_RUNTIME_VERSION" not in os.environ: will return False so we are in Databricks
- 
"""