# el-wiktionary-parser
A parser for el.wiktionary.org monthly dumps that creates a word
conjugator and POS tagger for greek words.

To use:
# #1. Download one of the el.wiktionary.org monthly dumps.
# #2. To create the json file with all words, run
```bash
greekdict.py /path/to/elwiki.xml
```
# #3. From your python code
```python
from greekdict import WikiWordGraph
word_graph = WikiWordGraph('word_graph.json')
nominative = word_graph[u'νερών']
pos = word_graph.get_pos(u'νερών')
```

