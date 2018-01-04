import sys
reload(sys)
sys.setdefaultencoding('utf8')

import textract
from textblob import TextBlob
from unidecode import unidecode

#text = textract.process("short.txt")
text = textract.process("book.txt")
text = unidecode(text)


import string
printable = set(string.printable)
text = filter(lambda x: x in printable, text)

blob = TextBlob(text)
#print(blob.tags)

#print("="*50)

#print(blob.noun_phrases)

npc = blob.np_counts

for key, value in sorted(npc.iteritems(), key=lambda (k,v): (v,k)):
  if (value > 1):
    print "%s: %s" % (key, value)


"""
import nltk
allWords = nltk.tokenize.word_tokenize(text)
allWordDist = nltk.FreqDist(w.lower() for w in allWords)

stopwords = nltk.corpus.stopwords.words('english')
print stopwords
allWordExceptStopDist = nltk.FreqDist(w.lower() for w in allWords if w not in stopwords)
print allWordExceptStopDist.pprint()
"""
