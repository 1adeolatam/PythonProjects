#!/usr/bin/env python
import sys
import random

#remove double spaces from file input
def readFile(flnm):
	with open(flnm,"r") as file:
		src = file.read().replace('\n\n','\n').replace(':',' ').replace(';',' ')
	return src

def makeChain(src, chain = {}):
	words = src.split(' ')
	index = 1# start from second entry and use first entry as key
	for word in words[index:]:
		key = words[index - 1]#the previous word
		if key in chain:
			chain[key].append(word)
		else:
			chain[key] = [word]
		index += 1
	return  chain

def generateMsg(chain, wordcount = 20):
	word1 = random.choice(list(chain.keys()))
	msg = word1
	
	while len(msg.split(' ')) < wordcount :
		word2 = random.choice(chain[word1])
		word1 = word2
		msg += ' ' + word2

	return msg
		
def writeFile(msg, flnm):
	with open(flnm,"w") as file:
		file.write(msg)


if __name__ == '__main__':
	if len(sys.argv) != 4:
		print("python markovSentence.py InputFileName MsgLength OutputFileName ")
		exit
	source = readFile(sys.argv[1])
	mchain = makeChain(source)
	generated = generateMsg(mchain,int(sys.argv[2]))
	writeFile(generated,sys.argv[3])
