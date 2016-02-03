#! /usr/bin/python

import sys
import string

alphabet = string.ascii_uppercase

def calculTableMultiplicationModulo(n) :
    #return [[i*j%n for i in range(n)] for j in range(n)]
    
    listA = list()
    listB = list()
    for i in range(n) :
        listA = list()
        for j in range(n) :
            listA.append((i*j)%n)
        listB.append(listA)
    return listB


def calculInverse(m, n) :
    listeMult = calculTableMultiplicationModulo(n)
    for i in range(n) :
        if listeMult[m%n][i] == 1 :
            return i

def listDiviseurs(n) :
    return [i for i in range(1,n) if n%i == 0]

def pgcd(m,n) :
    return max(list(set(listDiviseurs(m)) & set(listDiviseurs(n))))


def frequence(nomFichier) :
    cptLettre = 0
    frequence = dict([(alphabet[i], 0) for i in range(len(alphabet))])
    file = open(nomFichier, "r")
    texte = file.read().upper()
    file.close()
    for c in range(len(texte)) :
        if(texte[c].isalpha()) :
            cptLettre += 1
            frequence[texte[c]] += 1

    for cle, valeur in frequence.items() :
        frequence[cle] = (float(valeur) / float(cptLettre)) * 100
    
    return frequence

def write_frequency(frequency, filename) :
    file = open(filename, "w")
    for key, value in frequency.items() :
        file.write(key + " " + str(value) + "\n")
    file.close()
        


frequency = frequence("text/english/The Kama Sutra.txt")
write_frequency(frequency, "TheKamaSutra_frequency.txt")

