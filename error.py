from enchant.checker import SpellChecker
chkr=SpellChecker("en_US")
with open ("ess1.txt", "r") as myfile:
    text=myfile.read()
#essay=open('ess1.txt','r')
#text=essay.readline();
chkr.set_text(text)
ef=open('spell_err.txt','w')
for err in chkr:
    print('ERROR:',err.word)
    ef.write(str(err.word)+'\n')
ef.close()
