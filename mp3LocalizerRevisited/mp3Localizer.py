#!/usr/bin/env python
import eyed3
import sys


#def getTag(flnm):	
	#if eyeD3.isMp3File(flnm):
	#	audioFile= eyeD3.Mp3AudioFile(flnm)
	#	tag = audioFile.getTag()
#return tag#



if __name__ == '__main__':	
	audioFile = eyed3.load(sys.argv[1])
	print(audioFile.tag.artist)
	print(audioFile.tag.album)
	print(audioFile.tag.genre)
