#! /usr/bin/python

import sys
import string

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

