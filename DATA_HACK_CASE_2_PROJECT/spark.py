from pyspark.sql import SparkSession
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

spark = SparkSession.builder.getOrCreate()

#parquetF = spark.read.parquet("example.parquet")

#parquetF.show()

data =[("James ","","Smith","36636","M",3000),
              ("Michael ","Rose","","40288","M",4000),
              ("Robert ","","Williams","42114","M",4000),
              ("Maria ","Anne","Jones","39192","F",4000),
              ("Jen","Mary","Brown","","F",-1)]
#columns=["firstname","middlename","lastname","dob","gender","salary"]
#df = spark.createDataFrame(data, columns)
#df.write.parquet("people.parquet")
#parDF1 = spark.read.parquet("people.parquet")
#df.write.mode('append').parquet("people.parquet")
#df.write.mode('overwrite').parquet("people.parquet")
#parDF1.createOrReplaceTempView("ParquetTable")
#parkSQL = spark.sql("select * from ParquetTable where salary >= 4000 ")
#spark.sql("CREATE TEMPORARY VIEW PERSON USING parquet OPTIONS (path "/exemple.parquet")")
#spark.sql("SELECT * FROM PERSON").show()

#df = spark.createDataFrame([("a", 1),   ("b", 2), ("c",  3)], ["Col1", "Col2"])
#df.select(df.colRegex("(Col1)?+.+")).show()

peopleDF = spark.read.json("data.json")

# DataFrames can be saved as Parquet files, maintaining the schema information.
peopleDF.write.parquet("people.parquet")

# Read in the Parquet file created above.
# Parquet files are self-describing so the schema is preserved.
# The result of loading a parquet file is also a DataFrame.
parquetFile = spark.read.parquet("people.parquet")

# Parquet files can also be used to create a temporary view and then used in SQL statements.
parquetFile.createOrReplaceTempView("parquetFile")
teenagers = spark.sql("SELECT * FROM parquetFile ")
teenagers.show()