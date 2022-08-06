from pyspark.sql import SparkSession
import pandas as pd

spark = SparkSession.builder.getOrCreate()

#parquet_file = r'userdata1.parquet'
#pd.read_parquet(parquet_file, engine='auto')
#data1=spark.read.json("data.json")
#data1.show()
parquetF = spark.read.parquet("example.parquet")
parquetF.show()
