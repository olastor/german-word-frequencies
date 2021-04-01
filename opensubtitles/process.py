#/usr/bin/env python3

import nltk
import json
import pandas as pd
from collections import defaultdict

# create word frequency mapping using opensubtitle data and cistem stemmer

DATA_FILE = './de.txt' # download from http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.de.gz

freq = defaultdict(int)

stemmer = nltk.stem.Cistem()

def preprocess(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    return stemmer.stem(s)

def process(line):
  for token in nltk.word_tokenize(line, language='german'):
    token = token.strip()

    if not token:
      continue

    freq[token] += 1

with open(DATA_FILE) as f:
  for line in f:
    process(line)

df = pd.DataFrame(freq.items(), columns=['word', 'freq'], index=['word'])
df.to_csv('opensubtitles_cistem_freq.csv')
