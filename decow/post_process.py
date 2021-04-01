#!/usr/bin/env python3
import pandas as pd
from glob import glob

# merge result files from process.py into one file

dfs = []
for fn in glob('results/*'):
    if path.basename(fn) == '_SUCCESS':
        continue

    with open(fn) as f:
        dfs.append(pd.read_csv(fn, sep='\t', names=['word', 'freq'], index_col='word'))

    print(fn)

df_freq = pd.concat(dfs)
df_freq.to_csv('decow_cistem_freq.csv')
