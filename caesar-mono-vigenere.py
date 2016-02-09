#! /usr/bin/python

import sys
import string

alphabet = string.ascii_uppercase

def chiffrement_cesar (message, cle):
    message = message.upper()
    dec = (ord(cle.upper()) - ord('A'))%len(alphabet)
    message_chiffre = ""
    for x in message :
         message_chiffre += chr(((ord(x) - ord('A') + dec )%len(alphabet)) + ord('A'))
    return message_chiffre


def chiffrement_cesar_bis (message, cle):
    message = message.upper()
    dec = (ord(cle.upper()) - ord('A'))%len(alphabet)
    alphabet_dec = alphabet[dec:] + alphabet[:dec]
    return message.translate(string.maketrans(alphabet, alphabet_dec))
	
	
mes="BonjourParis"
print (chiffrement_cesar(mes, 'b'))
print (chiffrement_cesar_bis (mes, 'b'))