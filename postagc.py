import nltk
from nltk import word_tokenize, pos_tag
with open ("ess1.txt", "r") as myfile:
    text=myfile.read()
word=word_tokenize(text)
pos=pos_tag(word)
print(pos)
ncount=0;
vcount=0;
#nf=open('nouns.txt','w')
#vf=open('verbs.txt','w')
pf=open('pos_tags.txt','w')
for i in range(0,len(pos)):
    pf.write(str(pos[i])+'\n')
    #if ((pos[i][1]=='NN') or ( pos[i][1]=='NNS')):
    #    ncount+=1
    #    nf.write(pos[i][0]+'\n')
#print(ncount)
#for i in range(0,len(pos)):
#    if (pos[i][1]=='VB'):
#        vcount+=1
#        vf.write(pos[i][0]+'\n')
#nf.close()
#vf.close()
pf.close()

    
