#! /usr/bin/python

import sys
import string

alphabet = string.ascii_uppercase

def frequency(text) :
    nbletter = 0
    frequency = dict([(alphabet[i], 0) for i in range(len(alphabet))])
    for c in text :
        if c in alphabet :
            nbletter += 1
            frequency[c] += 1

    for key, value in frequency.items() :
        frequency[key] = (float(value) / float(nbletter)) * 100
    
    return frequency

def frequency_fromFile(filename) :
    file = open(filename, "r")
    text = file.read().upper()
    file.close()
    return frequency(text)
	
def format_frequency(frequency) :
    ret = ""
    for key, value in frequency.items() :
        ret += key + " " + str(value) + "\n"
    return ret

if __name__ == "__main__":
    frequencies = frequency(sys.argv[1])
    print(format_frequency(frequencies))
