#!/usr/bin/env python
#caesar cipher cracker


import sys
import string

key = string.printable

def readFile(flnm):
	with open(flnm,"r") as file:
		src = file.read().replace('\n\n','\n').replace(':',' ').replace(';',' ')
	return src


def encrypt(n, source):
	result = ''
	for l in source:
			i = (key.index(l) + n) % len(key)
			result += key[i]
	return result
	
def decrypt(ciphertext):
	final = ''
	for i in range(len(key)):
		decrypted = ''
		
		for symbol in ciphertext:			
			for j in range(len(key)):
				if ord(symbol) == j:
					break
				
			num = key.find(symbol)
			num -= i
			
			if num < 0:
				num += len(key)
				
			decrypted += key[num]
		final += decrypted +'\n'		
	return final

def writeFile(msg, flnm):
	with open(flnm,"w") as file:
		file.write(msg)


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("python markovSentence.py InputFileName Offset OutputFileName ")
		exit
	source = readFile(sys.argv[1])

	enc = encrypt(int(sys.argv[2])%len(key),source)
	writeFile(decrypt(enc),sys.argv[3])
