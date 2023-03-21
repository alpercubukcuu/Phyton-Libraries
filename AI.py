# -*- coding: utf-8 -*-
import pandas as pd

df = pd.read_csv("imdb_top_1000.csv")

print(df.head(5), df.tail(5), df.columns, df.dtypes)

