import numpy as np
import pandas as pd
pd.set_option("display.precision", 2)
pd.set_option('display.max_columns', None)



df = pd.read_csv('Data/ks-projects-201801.csv')
print(df['state'].value_counts())
