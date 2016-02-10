#! /usr/bin/python

import sys, string
from frequency import frequency
from caesar_mono_vigenere import *

fileFrench = "./text/french/germinal_nettoye.txt"
fileChiffre = "./text/extrait_chiffre.txt"

file = open(fileChiffre,"r")
message = file.read()

frequenceFrench = frequency(fileFrench)
frequenceChiffre = frequency(fileChiffre)

def trier(dico):
    items = dico.items()
    comparateur = lambda a,b : cmp(a[1],b[1])
    return sorted(items, comparateur, reverse=True)

def findKey(listFreqLangage, listFreqChiffre):
    key = alphabet
    for i in range(len(listFreqLangage)):
        key[ord(listFreqLangage[i][0])-ord('A')] = listFreqChiffre[i][0]
    return key
    

print(frequenceFrench)
print(frequenceChiffre)
listFreqLangage = trier(frequenceFrench)
listFreqChiffre = trier(frequenceChiffre)
key = findKey(listFreqLangage, listFreqChiffre)
clair = dechiffrement_mono(message, key)
print(clair)
