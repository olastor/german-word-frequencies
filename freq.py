import nltk
import json
from collections import defaultdict

DATA_FILE = './de.txt'

freq = defaultdict(int)

def process(line):
  for token in nltk.word_tokenize(line, language='german'):
    token = token.strip()
    
    if not token:
      continue

    freq[token] += 1

with open(DATA_FILE) as f:
  for line in f:
    process(line)

with open('freq_dist.json', 'w') as f:
  f.write(json.dumps(freq))
