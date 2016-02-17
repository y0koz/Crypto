#! /usr/bin/python

import sys, string
from frequency import *
from caesar_mono_vigenere import *

languages = {"english":"./text/engligh/TheKamaSutra.txt", "french":"./text/french/La_vie_sur_Mars.txt"}


def trier(dico):
    items = dico.items()
    comparateur = lambda a,b : cmp(a[1],b[1])
    return sorted(items, comparateur, reverse=True)

def guessKey_mono(listFreqLangage, listFreqChiffre):
    key = list(alphabet)
    for i in range(len(listFreqLangage)):
        key[ord(listFreqLangage[i][0])-ord('A')] = listFreqChiffre[i][0]
    return "".join(key)
   
if __name__ == "__main__":
    frequenceLanguage = frequency_fromFile(languages[sys.argv[1]])
    frequenceChiffre = frequency_fromFile(sys.argv[2])
    with open(sys.argv[2],'r') as f:
        chiffre = f.read()
    print(frequenceLanguage)
    print(frequenceChiffre)
    listFreqLangage = trier(frequenceLanguage)
    listFreqChiffre = trier(frequenceChiffre)
    print(listFreqLangage)
    print(listFreqChiffre)
    key = guessKey_mono(listFreqLangage, listFreqChiffre)
    message = dechiffrement_mono(chiffre, key)
    print(key)
    print(message)

