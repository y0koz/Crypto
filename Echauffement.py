#! /usr/bin/python

import sys
import string

#from string import maketrans

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
    for c in texte :
        if c in alphabet :
            cptLettre += 1
            frequence[c] += 1

    for cle, valeur in frequence.items() :
        frequence[cle] = (float(valeur) / float(cptLettre)) * 100
    
    return frequence

def format_frequency(frequency) :
    ret = ""
    for key, value in frequency.items() :
        ret += key + " " + str(value) + "\n"
    return ret


def chiffrement_cesar (message, cle):
    message = message.upper()
    dec = (ord(cle.upper()) - ord('A'))%len(alphabet)
    print dec
    message_chiffre = ""
    for x in message :
         message_chiffre += chr(((ord(x) - ord('A') + dec )%len(alphabet)) + ord('A'))
    return message_chiffre


def chiffrement_cesar_Bis (message, cle):
    message = message.upper()
    dec = (ord(cle.upper()) - ord('A'))%len(alphabet)
    alphabet_dec = alphabet[dec:] + alphabet[:dec]
    return message.translate(string.maketrans(alphabet, alphabet_dec))
                             
    
    
#frequency = frequence(sys.argv[1])
#print(format_frequency(frequency))
mes="BonjourParis"
print (chiffrement_cesar(mes, 'b'))
print (chiffrement_cesar_Bis (mes, 'b'))
