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

def get_tokens(filename):
   with open(filename, 'r') as myfile:
       text = myfile.read()
       lowers = text.lower()
       #remove the punctuation using the character deletion step of translate
       no_punctuation = re.sub('[%s]' % string.punctuation,'',lowers)
       tokens = word_tokenize(no_punctuation)
       return tokens

term_freq_matrix=[]

with open ("ess1.txt", "r") as myfile:
    doc1=myfile.read()

with open ("ess2.txt", "r") as myfile:
    doc2=myfile.read()

tdm = textmining.TermDocumentMatrix()

tdm.add_doc(doc1)
tdm.add_doc(doc2)
for row in tdm.rows(cutoff=1):
    term_freq_matrix.append(row)
term_freq_matrix=numpy.array(term_freq_matrix)
#tokenize and remove stopwords
term_freq_matrix = numpy.delete(term_freq_matrix, 0, 0)
#print(term_freq_matrix)
tokens=get_tokens("ess1.txt")
filtered = [w for w in tokens if not w in stopwords.words('english')]
print(filtered)
##count = Counter(filtered)
##print(count.most_common(100))

