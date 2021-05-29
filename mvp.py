# Analisis explotatorio
import sys
import numpy as np
import pandas as pd


url = 'https://raw.githubusercontent.com/EY-Data-Science-Program/2021-Better-Working-World-Data-Challenge/main/notebooks/03_EY_challenge1/resources/challenge1_train.csv'


df = pd.read_csv(url)

print(df.head())
