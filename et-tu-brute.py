#################################################################
# Name: Nicole Robles
# Date: March 21, 2020
# Description: Et tu, Brute?
# Language: Python 2.7.15
#
# Commandline argument: python et-tu-brute.py < ciphertext.txt
#################################################################

from sys import stdin

# the alphabets
ALPHABET = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789`~!@#$%^&*()-_=+[{]}\|;:'\",<.>/? "
# ALPHABET = " -,;:!?/.'\"()[]$&#%012345789aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxyYzZ"

# threshold for checking correctness of deciphered text
THRESHOLD = .5

# dictionary file
DICTIONARY_FILE = "dictionary.txt"

# performs a rotation (rot) of the alphabet
# rotated alphabet is used to produce a plaintext possibility
def rot(ciphertext, shift):
    # shifted (rotated) alphabet
    BETABET = ALPHABET[shift:] + ALPHABET[:shift]
    # plaintext possibility
    possibility = ""

    # go through every letter in the ciphertext
    for letter in ciphertext:
        # check to see if letter is found in the alphabet
        if letter in ALPHABET:
            # find the index of the letter in the real alphabet
            result = ALPHABET.find(letter)
            # find the corresponding letter in the rotated alphabet (BETABET)
            # add the corresponding letter to the plaintext possibility string
            possibility += BETABET[result]

        # if the letter is not in the alphabet, it must be a new line character
        else:
            possibility += "\n"

    return possibility

# read in the dictionary
f = open(DICTIONARY_FILE, "r")
dictionary = f.read().rstrip("\n").lower().split("\n")
f.close()

# read in the ciphertext
ciphertext = stdin.read().rstrip("\n")
# full ciphertext for full deciphering at the end
fullciphertext = "\n".join(ciphertext.split("\n"))
# efficient ciphertext for calculations
ciphertext = "\n".join(ciphertext.split("\n")[:10])

# for every letter in the alphabet
for i in range(1, len(ALPHABET)):
    # rotate the alphabet and output a plaintext possibility
    plaintext = rot(ciphertext, i)
    words = plaintext.lower().split(" ")

    # count the number of words in the plaintext possibility that appear in the dictionary
    count = 0
    for word in words:
        if word in dictionary:
            count += 1

    # if the count of words that are in the dictionary is above the threshold, print deciphered result
    if (count > len(words) * THRESHOLD):
        print "SHIFT={}: \n{}".format(len(ALPHABET)-i, "".join(rot(fullciphertext, i)))
