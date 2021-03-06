#! /usr/bin/python

from Echauffement import *

def matriceTodico(mat):
    ADFGVX = "ADFGVX"
    dico = dict()
    for i in range(len(ADFGVX)):
        for j in range(len(ADFGVX)):
            dico[mat[i][j]] = ADFGVX[i] + ADFGVX[j]
    return dico

def chiffreCaractere(dico, carac):
    return dico[carac]

def chiffreChaine(dico, chaine):
    chiffre = ""
    for i in range(len(chaine)):
        chiffre += chiffreCaractere(dico, chaine[i])
    return chiffre

def inverseClePermu(cle):
    copyCle = cle
    for i in range(len(cle)):
        copyCle[i] -= 1
    reversedCle = [i for i in range(len(cle))]
    for i in cle:
        reversedCle[copyCle[i]] = i
    return reversedCle

def permuterChaine(clePermu, chaine):
    chainePermutee = ""
    chainePermuteeHautBas = ""
    revClePermu = inverseClePermu(clePermu)
    print revClePermu
    while((len(chaine)%len(clePermu)) != 0):
        chaine += "X"
    ind = len(chaine)/len(clePermu)
    startSub = 0
    for i in range(ind):
        tmpChaine = ""
        subChaine = chaine[startSub:startSub + len(clePermu)]
        print subChaine
        for j in range(len(clePermu)):
            chainePermutee += subChaine[revClePermu[j]]
        startSub += len(clePermu)
    
    for i in range(ind):
        for j in range(ind):
            chainePermuteeHautBas += chainePermutee[(i+j*len(clePermu))]

    return chainePermuteeHautBas


def chiffrementADFGVX(message, matrice, clePermutation):
    return permuterChaine(clePermutation, chiffreChaine(matriceTodico(matrice), message))

"""def dechiffrementADFGVX(message, matrice, clePermutation) :
    nbLine = len(message)/len( clePermutation)
    permutedTab=["" for i in range(nbLine)]
    for j in range(len(message)) :
        permutedTab[j%(len( clePermutation))]+=message[j]
    clePermutation = len( clePermutation)
    for i in range(len clePermutation) :
         clePermutation[i] -= 1
    originalTab = []
    ADFmessage = ""
    for i in range(nbLine) :
        originalTab.append(permut(permutedTab[i], clePermutation))
        ADFmessage += originalTab[i]
    message = ""
    for i in range(len(ADFmessage)/2) :
        message += matrice[eq_ADF_index[ADFmessage[i*2]]][eq_ADF_index[ADFmessage[i*2+1]]]
    print message"""


matrice = [
    ['c','l','o','f','w','j'],
    ['y','m','t','5','b','4'],
    ['i','7','a','2','8','s'],
    ['p','3','0','q','h','x'],
    ['k','e','u','l','6','d'],
    ['v','r','g','z','n','9']
]   

message = "attaque"
clePermutation = [3,1,2,4]

print chiffrementADFGVX(message, matrice, clePermutation)

def chiffrementAffine(message, cle):
    if(pgcd(cle[0], 26) != 1):
        print 'La valeur a %d de la cle doit etre premier avec 26' % cle[0]
        return
    else :
        chiffre = ""
        message = message.upper()
        for i in range(len(message)):
            codelettre = ord(message[i]) - ord('A')
            codelettre = (((codelettre*cle[0]) + cle[1]) % 26) 
            chiffre += chr(ord('A') + (codelettre))
        return chiffre

def dechiffrementAffine(chiffre, cle):
    message = ""
    chiffre = chiffre.upper()
    inverseCle = calculInverse(cle[0], 26)
    for i in range(len(chiffre)):
        codelettre = ord(chiffre[i]) - ord('A')
        codelettre = (((codelettre-cle[1])*inverseCle) % 26) 
        message += chr(ord('A') + (codelettre))
    return message


message = "toto"
cle = (3, 15)
chiffre = chiffrementAffine(message, cle)
print 'Chiffre de toto: ' + chiffre
print calculInverse(cle[0], 26)
print 'Dechiffre de ' + chiffre + ' : ' + dechiffrementAffine(chiffre, cle)