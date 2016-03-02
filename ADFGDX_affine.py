#! /usr/bin/python

matrice = [
    ['c','l','o','f','w','j'],
    ['y','m','t','5','b','4'],
    ['i','7','a','2','8','s'],
    ['p','3','0','q','h','x'],
    ['k','e','u','l','6','d'],
    ['v','r','g','z','n','9']
]

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
    for i in range(len(cle)):
        cle[i] -= 1
    reversedCle = [i for i in range(len(cle))]
    for i in cle:
        reversedCle[cle[i]] = i
    return reversedCle

def permuterChaine(clePermu, chaine):
    chainePermutee = ""
    revClePermu = inverseClePermu(clePermu)
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
    return chainePermutee
    

message = "attaque"
clePermutation = [3,1,2,4]

dico = matriceTodico(matrice)
print dico
chiffre = chiffreChaine(dico, message)
print chiffre
revCle = inverseClePermu(clePermutation)
print revCle
permut = permuterChaine(clePermutation, chiffre)
print permut

    

