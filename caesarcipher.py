#!/usr/bin/env python
#caesar cipher cracker


import sys
import string

key = string.printable


def encrypt(n, source):
	result = ''
	for l in source.lower():
			i = (key.index(l) + n) % len(key)
			result += key[i]
	return result.lower()
	
def decrypt(ciphertext):
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
				
		print('Key #%s: %s'%(i,decrypted))


src = input("enter source text\n")
offset = int(input("enter num between 1 and %s\n"%len(key)))

enc = encrypt(offset,src)
print(src)
print("The encrypted text is: \n")
print(enc)
print("\n")

decrypt(enc)
