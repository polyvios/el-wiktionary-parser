#!/usr/bin/python3
# -*- coding: utf-8 -*-

##########################################################################
#                                                                        #
# The MIT License (MIT)                                                  #
#                                                                        #
# Copyright (c) 2016-2020 Polyvios Pratikakis <polyvios@gmail.com>       #
#                                                                        #
# Permission is hereby granted, free of charge, to any person            #
# obtaining a copy of this software and associated documentation files   #
# (the "Software"), to deal in the Software without restriction,         #
# including without limitation the rights to use, copy, modify, merge,   #
# publish, distribute, sublicense, and/or sell copies of the Software,   #
# and to permit persons to whom the Software is furnished to do so,      #
# subject to the following conditions:                                   #
#                                                                        #
# The above copyright notice and this permission notice shall be         #
# included in all copies or substantial portions of the Software.        #
#                                                                        #
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,        #
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF     #
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND                  #
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE #
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION #
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION  #
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.        #
##########################################################################

###
# Greek word conjugation and declination
#
# @author Polyvios Pratikakis <polyvios@gmail.com>
#
# Example Usage of wiktionary pos-tagger
#

import sys
import optparse
import pprint
from greekdict import WikiWordGraph

#class MyPrettyPrinter(pprint.PrettyPrinter):
#  def format(self, object, context, maxlevels, level):
#    if isinstance(object, unicode):
#      return (object.encode('utf8'), True, False)
#    return pprint.PrettyPrinter.format(self, object, context, maxlevels, level)
#
#gprint = MyPrettyPrinter(width=400).pprint

if __name__ == u'__main__':
  parser = optparse.OptionParser(usage="Usage: %prog < text")
  parser.add_option("-i", "--input", action="store", dest="input", default=u'word_graph.json', help="Where to get the word graph.")
  (options, args) = parser.parse_args()

  if len(args) == 0:
    parser.print_help()
    sys.exit(1)

  word_graph = WikiWordGraph(options.input)
  text = [w for w in args]
  sentence = []
  for word in text:
    print("\n ", word)
    nominative = word_graph[word]
    pos = word_graph.get_pos(word)
    print(" ", nominative)
    print(" ", pos)
    if pos is not None and u'Συν' in pos:
      print(sentence)
      sentence = []
    else:
      sentence.append(word)
  print(sentence)
