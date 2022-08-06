import pyarrow.parquet as pq
import numpy as np
import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.DataFrame({'one': [-1, np.nan, 2.5],
                   'two': ['foo', 'bar', 'baz'],
                   'three': [True, False, True]},
                   index=list('abc'))


table = pa.Table.from_pandas(df)
pq.write_table(table, 'example.parquet')
table2 = pq.read_table('example.parquet')

table2.to_pandas()
pq.read_table('example.parquet', columns=['one', 'three'])
pq.read_pandas('example.parquet', columns=['two']).to_pandas()