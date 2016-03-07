import nltk
from nltk import word_tokenize, pos_tag
with open ("ess1.txt", "r") as myfile:
    text=myfile.read()
word=word_tokenize(text)
pos=pos_tag(word)
#print(pos)
ncount=0;
vcount=0;
acount=0;
nf=open('nouns.txt','w')
vf=open('verbs.txt','w')
af=open('adj.txt','w')
nc=open('nc.txt','w')
vc=open('vc.txt','w')
ac=open('ac.txt','w')
for i in range(0,len(pos)):
    if ((pos[i][1]=='NN') or ( pos[i][1]=='NNS')):
        ncount+=1
        nf.write(pos[i][0]+'\n')
print(ncount)
for i in range(0,len(pos)):
    if (pos[i][1]=='VB'):
        vcount+=1
        vf.write(pos[i][0]+'\n')
for i in range(0,len(pos)):
    if (pos[i][1]=='JJ'):
        acount+=1
        af.write(pos[i][0]+'\n')
nc.write(str(ncount))
vc.write(str(vcount))
ac.write(str(acount))
nf.close()
vf.close()
af.close()
nc.close()
vc.close()
ac.close()
