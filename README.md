# German Word Frequencies

Simple word to frequency mappings for the german language based on text corpora and using CISTEM stemmer. May be useful for various purposes.

## Data

### cow16 (~ 42 million unique stemmed words)

The source data already contains a frequency list, but still was preprocessed using the routine in the `decow/` folder.

**Word Frequencies**

 - [decow_wordfreq_cistem.csv.7z](https://nlp-data-filestorage.s3.eu-central-1.amazonaws.com/word-frequencies/decow_wordfreq_cistem.csv.7z) (203MB, 672MB uncompressed)
   - md5sum: 5b2797838221fbb9518f2800deee60d4

**License & Attribution**

The original corpus is licensed under Creative Commons Attribution 4.0.

- [License](https://www.webcorpora.org/opendata/frequencies/german/decow16b/LICENSE)
- [README](https://www.webcorpora.org/opendata/frequencies/german/decow16b/README)
- [Schäfer (2015)](http://rolandschaefer.net/?p=749) and [Schäfer & Bildhauer (2012)](http://rolandschaefer.net/?p=70)

### opensubtitles (~ 900k unique stemmed words)

**Word Frequencies**

 - [opensubtitles_cistem_freq.csv](https://github.com/olastor/german-word-frequencies/blob/main/opensubtitles/opensubtitles_cistem_freq.csv?raw=true) (13MB)
   - md5sum: 7cceeaa18a8c519848ceff88350a9aef

**License & Attribution**

P. Lison and J. Tiedemann, 2016, OpenSubtitles2016: Extracting Large Parallel Corpora from Movie and TV Subtitles. In Proceedings of the 10th International Conference on Language Resources and Evaluation (LREC 2016)

## Example Usage

Download and extract one of the archives. Then use it like this (warning: this way it may use much memory):

```python
import pandas as pd
import nltk

word = 'Onlineumfrage'

stemmer = nltk.stem.Cistem()
df = pd.read_csv('~/decow_wordfreq_cistem.csv', index_col=['word'])
df.at[stemmer.stem(word), 'freq'] # => 8490
```
