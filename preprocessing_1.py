import csv
import pandas as pd
import numpy as np

df = pd.read_csv("Dwarf Brown Stars.csv")

star_df = df[df["Name"].notna()]
star_df = df[df["Distance"].notna()]
star_df = df[df["Mass"].notna()]
star_df = df[df["Radius"].notna()]
star_df.pop('Unnamed: 0')

star_df["Radius"] = star_df["Radius"]*0.102763 
star_df["Mass"] = star_df["Mass"].astype('float64')*0.000954588

star_df.to_csv("Dwarf-Brown-Stars.csv")