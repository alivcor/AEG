import nltk
import csv
import numpy
from nltk import word_tokenize, pos_tag
with open ("ess1.txt", "r") as myfile:
    text=myfile.read()
word=word_tokenize(text)
print(word)
# Open a file
#fo = open("tokenscs.csv", "wb")
#fo.write(word);
#a = word.toarray()
#numpy.savetxt("tokenscs.csv", word, delimiter=",")
# Close opend file
#fo.close()
#with open("tokenscs.csv", "wb") as f:
#    writer = csv.writer(f)
#    writer.writerows(word)
#myfile = open("tokenscs.csv", "w")
#wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
#wr.writerow(word)
w=open('words.txt','w')
for i in range(0,len(word)):
        w.write(word[i]+'\n')
w.close()
