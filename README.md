# el-wiktionary-parser
A parser for el.wiktionary.org monthly dumps that creates a word
conjugator and POS tagger for greek words.

To use:
# #1. Download one of the el.wiktionary.org monthly dumps.
```bash
wget https://dumps.wikimedia.org/elwiktionary/latest/elwiktionary-latest-pages-articles-multistream.xml.bz2
```
# #2. To create the `word_graph.json` file with all words, run
```bash
greekdict.py elwiktionary-latest-pages-articles-multistream.xml.bz2
```
# #3. From your python code
```python3
from greekdict import WikiWordGraph
word_graph = WikiWordGraph('word_graph.json')
nominative = word_graph[u'νερών']
pos = word_graph.get_pos(u'νερών')
```

