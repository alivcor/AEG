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

term_freq_matrix=[]

f1 = open("DataSet/trsetmodified.txt", "r")
essr = csv.reader(f1)
count=1
for row in essr:
    fname = "DataSet/Essays/ess" + str(count) + ".txt"
    f2 = open(fname,"w")
    essw = csv.writer(f2)
    essw.writerow(row)
    f2.close()
    count=count+1
    #print(row)

tdm = textmining.TermDocumentMatrix()

for num in range(1,100):
    fname = "DataSet/Essays/ess" + str(num) + ".txt"
    with open (fname, "r") as myfile:
        doc1=myfile.read()
        tdm.add_doc(doc1)

f2 = open("most_common_words.txt","w")
essw = csv.writer(f2)
for row in tdm.rows(cutoff=2):
    term_freq_matrix.append(row)
    essw.writerow(row)
f2.close()
term_freq_matrix=numpy.array(term_freq_matrix)
#tokenize and remove stopwords
#term_freq_matrix = numpy.delete(term_freq_matrix, 0, 0)
print(term_freq_matrix)




