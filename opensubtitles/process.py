#!/usr/bin/env python3
import pyspark
import nltk
import string

# create word frequency data from decow using cistem stemmer for preprocessing

stemmer = nltk.stem.Cistem()

def preprocess(s):
    s = s.translate(str.maketrans('', '', string.punctuation))
    return stemmer.stem(s)

def map_line(line):
  tokens = [preprocess(token) for token in nltk.word_tokenize(line, language='german')]
  return [t for t in tokens if t]

sc = pyspark.SparkContext(appName="word_freq")

distFile = sc.textFile("./de.txt") # download from http://opus.nlpl.eu/download.php?f=OpenSubtitles/v2018/mono/OpenSubtitles.raw.de.gz

distFile.flatMap(map_line).map(lambda x: (x, 1)).reduceByKey(lambda a, b: a + b).map(lambda k: k[0] + '\t' + str(k[1])).saveAsTextFile('results')
