import csv
import textmining
import numpy 
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from nltk.corpus import stopwords
from nltk import word_tokenize, pos_tag
from collections import Counter
import string
import re
numpy.set_printoptions(threshold=numpy.nan)

def get_tokens(filename):
   with open(filename, 'r') as myfile:
       text = myfile.read()
       lowers = text.lower()
       #remove the punctuation using the character deletion step of translate
       no_punctuation = re.sub('[%s]' % string.punctuation,'',lowers)
       tokens = word_tokenize(no_punctuation)
       return tokens



f1 = open("DataSet/trsetmodified.txt", "r")
essr = csv.reader(f1)
count=1
for row in essr:
    fname = "DataSet/thebigessay.txt"
    f2 = open(fname,"a")
    essw = csv.writer(f2)
    essw.writerow(row)
    f2.close()
    count=count+1
    #print(row)

tokens=get_tokens("DataSet/thebigessay.txt")
filtered = [w for w in tokens if not w in stopwords.words('english')]
print(filtered)
count = Counter(filtered)
print(count.most_common(100))



