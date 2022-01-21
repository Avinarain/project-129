import csv
import pandas as pd

df = pd.read_csv("Bright Stars.csv")

star_df = df.dropna()
star_df.pop('Sr No')
star_df.to_csv("Bright-Stars.csv")