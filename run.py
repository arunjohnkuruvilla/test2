import dump
import sys
import md5
import time
import hashlib

def characters():
	global CHARACTERS_FILENAME
	char_file = open(CHARACTERS_FILENAME, 'r')
	chars = []
	for line in char_file:
		chars.append(line[:-1])
	return chars

def check(keyword, check_list):
	m = hashlib.sha256()
	m.update(keyword)
	test_hash = m.hexdigest()
	result = []
	print "%s : %s" % (keyword, test_hash)
	if test_hash in check_list:
		result.append(1)
		result.append(keyword)
		result.append(test_hash)
	else:
		result.append(0)
	return result

def make_keywords():
	global HASH_FILENAME
	data = dump.build_data(HASH_FILENAME)
	keywords = []
	chars = characters()

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,7):
		if x == 1:																# Strings of length 1
			if size_one == 0:
				size_one = 1
				print "Trying strings of length 1..."
			for char1 in chars:
				for x in xrange(0,100):
					string = char1
					string = string +  str(format(x, '02d'))
					check_result = check(string, data)
					if(check_result[0]):
						results[check_result[1]] = check_result[2]
				#keywords.append(string)
		if x == 2:																# Strings of length 2
			if size_two == 0:
				size_two = 1
				print "Completed strings of length 1."
				print "Trying strings of length 2..."
			for char1 in chars:
				for char2 in chars:
					for x in xrange(0,100):
						string = char1 + char2
						string = string +  str(format(x, '02d'))
						check_result = check(string, data)
						if(check_result[0]):
							results[check_result[1]] = check_result[2]
					#keywords.append(string)
		if x == 3:																# Strings of length 3
			if size_three == 0:
				size_three = 1
				print "Completed strings of length 2."
				print "Trying strings of length 3..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for x in xrange(0,100):
							string = char1 + char2 + char3
							string = string +  str(format(x, '02d'))
							check_result = check(string, data)
							if(check_result[0]):
								results[check_result[1]] = check_result[2]
						#keywords.append(string)
		if x == 4:																# Strings of length 4
			if size_four == 0:
				size_four = 1
				print "Completed strings of length 3."
				print "Trying strings of length 4..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for x in xrange(0,100):
								string = char1 + char2 + char3 + char4
								string = string +  str(format(x, '02d'))
								check_result = check(string, data)
								if(check_result[0]):
									results[check_result[1]] = check_result[2]
							#keywords.append(string)
		if x == 5:																# Strings of length 5	
			if size_five == 0:
				size_five = 1
				print "Completed strings of length 4."
				print "Loading strings of length 5..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for x in xrange(0,100):
									string = char1 + char2 + char3 + char4 + char5
									string = string +  str(format(x, '02d'))
									check_result = check(string, data)
									if(check_result[0]):
										results[check_result[1]] = check_result[2]
								#keywords.append(string)
		if x == 6:																# Strings of length 6
			if size_six == 0:
				size_six = 1
				print "Completed strings of length 5."
				print "Loading strings of length 6..."
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for x in xrange(0,100):
										string = char1 + char2 + char3 + char4 + char5 + char6
										string = string +  str(format(x, '02d'))
										check_result = check(string, data)
										if(check_result[0]):
											results[check_result[1]] = check_result[2]
									#keywords.append(string)
	print "Completed strings of length 5."
	return results

if __name__ == '__main__':

	HASH_FILENAME = "eHarmony.txt"
	CHARACTERS_FILENAME = "characters.txt"
	OUTPUT_FILENAME = "out.txt"
	
	if len(sys.argv) == 0 :
		print "Hash File not provided. Using Default Hash File"
	else:
		HASH_FILENAME = sys.argv[1]

	start = time.time()

	results = make_keywords()

	end = time.time()
	print (end - start)

	out_file = open(OUTPUT_FILENAME, "a")

	print "Results:"
	for key, value in results.iteritems():
		print key, value
		out_file.write("%s : %s" % (key, value))

	#for keyword in keywords:

