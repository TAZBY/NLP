
# coding: utf-8

# In[4]:


import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.tag.stanford import StanfordPOSTagger
root_path="nltkTools/"
pos_tagg = StanfordPOSTagger(root_path + "french.tagger", root_path + "stanford-postagger.jar",encoding='utf8') #instance de la classe StanfordPOSTagger en UTF-8


file = open("regles.txt")
lines = file.readlines()

file.close()

mot=str(input("Veuillez entrer un mot svp:"))

motokenizze = word_tokenize(mot)
mottagg = pos_tagg.tag(motokenizze)

#print(mottagg)
tag=""

for va in mottagg:
    tag=va[1]

#Pour les verbes
suffixe = mot[-2]+mot[-1]
nvlt = ""
typemot = ""
if(tag == 'V' or tag == 'VINF'):
    typemot = "un Verbe"
if(tag =='NC'):
    typemot = "un Nom Commun"
if(tag =='ADJ'):
    typemot = "un Adjectif"
if(tag =='DET'):
    typemot = "un Déterminant"
if(tag =='P'):
    typemot = "une Préposition"

print("Le mot que vous avez entré est : "+typemot)

prempartie=""
chainef = ""

for line in lines:
    line = line.strip()
    line = line.replace("*","")
    if len(line) != 0:
        lin = word_tokenize(line)
    
        for ligne in lin:
            nvlt = ligne
        if(tag == 'V' or tag == 'VINF'):
            if(len(lin[0])>2):
                if(lin[0] in mot):
                    mss = mot.replace(lin[0], nvlt)
                    print(mot+" -> "+mss)
                
            if(suffixe == lin[0]):
                mss = mot.replace(suffixe, nvlt)
                print(mot+" -> "+mss)
        elif(tag == 'ADJ'):
            if(lin[0] in mot):
                mss = mot.replace(lin[0], nvlt)
                print(mot+" -> "+mss)
        elif(tag == 'NC'):
            if(lin[0] in mot):
                mss = mot.replace(lin[0], nvlt)
                print(mot+" -> "+mss)
        elif(tag == 'ADV'):
            if(lin[0] in mot):
                mss = mot.replace(lin[0], nvlt)
                print(mot+" -> "+mss)
        elif(tag == 'DET'):
            if(lin[0] in mot):
                mss = mot.replace(lin[0], nvlt)
                print(mot+" -> "+mss)
        elif(tag == 'P'):
            if(lin[0] in mot):
                mss = mot.replace(lin[0], nvlt)
                print(mot+" -> "+mss)
            
        


