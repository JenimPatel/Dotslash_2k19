# -*- coding: utf-8 -*-
"""Untitled13.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1h8mbXaOaxY5C2LWvjHlaSvRkq9HHW8FB
"""

import spacy as sp
import nltk
from nltk.tokenize import sent_tokenize

nltk.download('punkt')
c = sent_tokenize("New Text Document.txt")

file_content = open("New Text Document.txt").read()
c = sent_tokenize(file_content)

k=[]
nlp = spacy.load('en') 
for i in range(len(c)):
  for j in range(i+1,len(c)-1):
    search_doc = nlp(c[i])
    main_doc = nlp(c[j])
    if(main_doc.similarity(search_doc)>=0.7):
      k.append(main_doc)
print(k)

for i in range(len(k)):
  k[i] = str(k[i])
for i in range(len(k)):
  if(k[i] in c):
    l = c.index(k[i])
    del c[l]

s=''
for i in range(len(c)):
  s=s+c[i]

