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
   word, pos, count = line.split('\t')
   return (preprocess(word), int(count))

sc = pyspark.SparkContext(appName="word_freq")

distFile = sc.textFile("./decow16bx.wp.tsv") # download from https://www.webcorpora.org/opendata/frequencies/german/decow16b/

distFile.map(map_line).filter(lambda k: k[0]).reduceByKey(lambda a, b: a + b).map(lambda k: k[0] + '\t' + str(k[1])).saveAsTextFile('results')
