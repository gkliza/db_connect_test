from pyspark.sql import SparkSession, DataFrame

class FlexEnv():

    def __init__(self, spark_session: SparkSession):
        self.spark = spark_session

    def show_catalogs(self) -> DataFrame:
        return self.spark.sql("SHOW CATALOGS")
