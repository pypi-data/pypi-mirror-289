import os
from pyspark.sql import SparkSession


def getSpark(driver_memory: str = "21g") -> SparkSession:
    spark = (
        SparkSession.builder
        # General
        .master('local[*]')
        .config("spark.driver.maxResultSize", 0)

        # Get 80% of free memory (this might be a bad idea)
        .config("spark.driver.memory", driver_memory)
        .config("spark.dynamicAllocation.enabled", "true")

        # PyArrow for dtypes conversions
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")

        # Jars compatible with the base-notebook image (Python 3.8, PySpark 3.3.2)
        .config('spark.jars.packages', 'org.apache.hadoop:hadoop-aws:3.3.2,io.delta:delta-core_2.12:2.2.0')

        # Delta Lake setup
        .config("spark.hadoop.fs.s3a.connection.maximum", 128)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore")
    )
    
    spark = spark.config(
        "fs.s3a.aws.credentials.provider",
        "com.amazonaws.auth.DefaultAWSCredentialsProviderChain"
    )
    return spark.getOrCreate()


def getGlue(driver_memory: str = "21g") -> SparkSession:
    spark = (
        SparkSession.builder
        # General
        .config("spark.driver.maxResultSize", 0)

        # Get 80% of free memory (this might be a bad idea)
        .config("spark.driver.memory", driver_memory)
        .config("spark.dynamicAllocation.enabled", "true")

        # PyArrow for dtypes conversions
        .config("spark.sql.execution.arrow.pyspark.enabled", "true")

        # Delta Lake setup
        .config("spark.hadoop.fs.s3a.connection.maximum", 128)
        .config("spark.sql.extensions", "io.delta.sql.DeltaSparkSessionExtension")
        .config("spark.sql.catalog.spark_catalog", "org.apache.spark.sql.delta.catalog.DeltaCatalog")
        .config("spark.delta.logStore.class", "org.apache.spark.sql.delta.storage.S3SingleDriverLogStore")

        # Glue setup
        .config("hive.metastore.client.factory.class", "com.amazonaws.glue.catalog.metastore.AWSGlueDataCatalogHiveClientFactory")
        .config("aws.region", os.environ.get('AWS_DEFAULT_REGION'))
        .config("hive.metastore.glue.catalogid", os.environ.get('GLUE_CATALOG_ID'))
        .enableHiveSupport()
    )

    return spark.getOrCreate()
