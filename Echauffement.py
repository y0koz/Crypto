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
    for j in range(len(texte)) :
        if(texte[j].isalpha()) :
            cptLettre += 1
            frequence[texte[j]] += 1

    for cle, valeur in frequence.items() :
        frequence[cle] = (float(valeur) / float(cptLettre)) * 100
    
    return frequence


n=12
m=8

print(calculTableMultiplication(12))
print(calculInverse(m,n))
print(listDiviseurs(n))
print(pgcd(m,n))
print(frequence("text/texte.txt"))
