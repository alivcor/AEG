import textmining
import numpy
import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
m=[]
p=0
doc1 = 'John and Bob are brothers.'
with open ("ess1.txt", "r") as myfile:
    doc1=myfile.read()
    #doc1=myfile.read().replace('\n', '')
doc2 = 'John went to the store. The store was closed.'
with open ("ess2.txt", "r") as myfile:
    doc2=myfile.read()
    #doc2=myfile.read().replace('\n', '')
#doc3 = 'Bob went to the store too.'
# Initialize class to create term-document matrix
tdm = textmining.TermDocumentMatrix()
# Add the documents
tdm.add_doc(doc1)
tdm.add_doc(doc2)
#tdm.add_doc(doc3)
# Write out the matrix to a csv file. Note that setting cutoff=1 means
# that words which appear in 1 or more documents will be included in
# the output (i.e. every word will appear in the output). The default
# for cutoff is 2, since we usually aren't interested in words which
# appear in a single document. For this example we want to see all
# words however, hence cutoff=1.
tdm.write_csv('matrix.csv', cutoff=1)
# Instead of writing out the matrix you can also access its rows directly.
# Let's print them to the screen.

for row in tdm.rows(cutoff=1):
    m.append(row)
    if p==1:
        arr = row
        #print("p")
        #print("arr=row")
        #print(arr)
        #print("")
        p=p+1
    if p>1:
        arr = numpy.vstack((arr, row))
        #print(p)
        #print("arr = numpy.vstack((arr, row))")
        #print(arr)
        #print("")
        p=p+1
    if p==0:
        #print(p)
        #print("Just Increment p .... Voila !")
        
        #print("")
        p=p+1
        #arr = numpy.delete(arr, (0), axis=0)


p=0
arr = numpy.delete(arr, (0), axis=0)
print("")
print("TDM:")
print(m)
print("")
print("")
print("")
print("TDM Sparse Matrix:")
print(arr)
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(arr)
a = tfidf.toarray()
numpy.savetxt("foo.csv", a, delimiter=",")
print(tfidf.toarray())
