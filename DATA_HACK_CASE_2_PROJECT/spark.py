from pyspark.sql import SparkSession
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

spark = SparkSession.builder.getOrCreate()

emp_data = [
    (1, "Alexander", 2, 3500),
    (2, "Roman", 1, 4500),
    (3, "Tom", 1, 5500),
    (4, "Alex", 3, 3000),
    (5, "Arthur", 4, 4250),
    (6, "Anna", 4, 3520),
    (7, "Svetlana", 2, 3000),
    (8, "Oleg", 5, 3200),
    (9, "Felix", 1, 5500),
    (10, "Olga", 5, 4970),
    (11, "Anna", 4, 6320),
    (12, "Tom", 3, 3500),
    (13, "Felix", 4, 3520),
    (14, "John", 2, 3500),
    (15, "Finn", 5, 5570),
    (16, "Polly", 3, 3800),
]

emp_schema = ["emp_id", "emp_name", "dept_id", "salary"]
dept_data = [
    (1, "IT"),
    (2, "Admin"),
    (3, "HR"),
    (4, "Finance"),
    (6, "Marketing"),
]
dept_schema = ["dept_id", "dept_name"]

df1 = pd.DataFrame(emp_data, columns=emp_schema)
df2 = pd.DataFrame(dept_data, columns=dept_schema)


df=pd.merge(df1, df2, on='dept_id', how='inner')

#print(df)

table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')

table2 = pq.read_table('example.parquet')

print(table2.to_pandas())
