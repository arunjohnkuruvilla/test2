#! /usr/bin/env python

import sys
import md5
import time
import stage0
import stage1
import stage2

if __name__ == '__main__':

	HASH_FILENAME = "eHarmony.txt"
	CHARACTERS_FILENAME = "characters.txt"
	OUTPUT_FILENAME = "out.txt"
	STAGE_NO = 1
	
	results = {}

	if len(sys.argv) <= 2 :
		print "No arguments provided. Using default values"
	else:
		HASH_FILENAME = sys.argv[1]
		STAGE_NO = int(sys.argv[2])
		OUTPUT_FILENAME = sys.argv[3]
		CHARACTERS_FILENAME = sys.argv[4]

	if(STAGE_NO == 0):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage0.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force strings of length 1-4
	if(STAGE_NO == 1):
		start = time.time()

		results = stage1.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	if(STAGE_NO == 2):
		start = time.time()

		results = stage1.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	if(STAGE_NO == 3):
		start = time.time()

		results = stage1.make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force PASSWORD + strings of length 1-3 + SALT
	if(STAGE_NO == 5):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage2.make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	#Brute force PASSWORD + strings of length 1-3 + SALT
	if(STAGE_NO == 6):
		PASSWORD_FILE = sys.argv[5]

		start = time.time()

		results = stage2.make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE)

		end = time.time()
		print "Brute-Force Strings of length 1 - 4 took: " + str(end - start)

	print "Results:"
	for key, value in results.iteritems():
		print key, value

	#for keyword in keywords:

