#! /usr/bin/python

import sys
import string
import random

alphabet = string.ascii_uppercase


"""def chiffrement_cesar_bis (message, cle):
    message = message.upper()
    dec = (ord(cle.upper()) - ord('A'))%len(alphabet)
    message_chiffre = ""
    for x in message :
         message_chiffre += chr(((ord(x) - ord('A') + dec )%len(alphabet)) + ord('A'))
    return message_chiffre"""

def normalize_key_cesar(key):
    """le cle peut être un caractère ou un entier indicant le décalage,
    si la cle est une chaine de longueur superieure à 1, 
    alors le premier caractère de celle-ci est utilisé comme cle."""
    if type(key) is int :
        return (key % len(alphabet))
    elif type(key) is str :
        if len(key) > 1 :
            key = key[0]
        return (ord(key.upper()) - ord('A'))%len(alphabet)
    else :
        print("Cle invalide")
        exit(-1)

def chiffrement_cesar(message, key):
    message = message.upper()
    dec = normalize_key_cesar(key)
    alphabet_dec = alphabet[dec:] + alphabet[:dec]
    return message.translate(string.maketrans(alphabet, alphabet_dec))

def dechiffrement_cesar(chiffre, key):
    chiffre = chiffre.upper()
    dec = normalize_key_cesar(key)
    alphabet_dec = alphabet[dec:] + alphabet[:dec]
    return chiffre.translate(string.maketrans(alphabet_dec, alphabet))

def getRandomAlphabet():
    key = list(alphabet)
    random.shuffle(key)
    return ''.join(key)

def chiffrement_mono(message, key):
    message = message.upper()
    return message.translate(string.maketrans(alphabet, key))

def dechiffrement_mono(chiffre, key):
    chiffre = chiffre.upper()
    return chiffre.translate(string.maketrans(key, alphabet))

def chiffrement_vigenere(message, key):
    message = message.upper()
    key = key.upper()
    chiffre = ""
    for i in range(len(message)):
        codelettre = ord(message[i]) - ord('A')
        decalage = ord(key[i%len(key)]) - ord('A')
        chiffre += chr(ord('A') + (codelettre + decalage)%len(alphabet))
    return chiffre

def dechiffrement_vigenere(chiffre, key):
    chiffre = chiffre.upper()
    key = key.upper()
    message = ""
    for i in range(len(chiffre)):
        codelettre = ord(chiffre[i]) - ord('A')
        decalage = ord('A') - ord(key[i%len(key)])
        message += chr(ord('A') + (codelettre + decalage)%len(alphabet))
    return message

if __name__ == "__main__":
    print("\n")
    message = "BonjourParis"
    print("Message: " + message)

    # César
    cleCesar = "b"
    print("Clé César: " + cleCesar)
    chiffreCesar = chiffrement_cesar(message, cleCesar)
    print("Chiffré César: " + chiffreCesar)
    dechiffreCesar = dechiffrement_cesar(chiffreCesar, cleCesar)
    print("Déchiffré César: " + dechiffreCesar)
    
    # Mono-alphabétique
    cleMono = getRandomAlphabet()
    print("Clé Mono: " + cleMono)
    chiffreMono = chiffrement_mono(message, cleMono)
    print("Chiffré Mono: " + chiffreMono)
    dechiffreMono = dechiffrement_mono(chiffreMono, cleMono)
    print("Déchiffré Mono: " + dechiffreMono)
    
    # Vigenère
    cleVigenere = "pass"
    print("Clé Vigenère: " + cleVigenere)
    chiffreVigenere = chiffrement_vigenere(message, cleVigenere)
    print("Chiffré Vigenère: " + chiffreVigenere)
    dechiffreVigenere = dechiffrement_vigenere(chiffreVigenere, cleVigenere)
    print("Déchiffré Vigenère: " + dechiffreVigenere)
