import sys
import md5
import time
import hashlib

def build_data(filename):
	dump_file = open(filename, "r")
	data = {}
	for line in dump_file:
		data[line[:-1]] = ""
	return data

def characters(CHARACTERS_FILENAME):
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
	print "%s" % (keyword)
	if test_hash in check_list:
		result.append(1)
		result.append(keyword)
		result.append(test_hash)
	else:
		result.append(0)
	return result

#All strings of length 1 - 4
def make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			for char1 in chars:
				for x in xrange(0,100):
					string = char1
					string = str(format(x, '02d')) + string
					check_result = check(string, data)
					if(check_result[0]):
						results[check_result[1]] = check_result[2]
		if x == 2:																# Strings of length 2
			for char1 in chars:
				for char2 in chars:
					for x in xrange(0,100):
						string = char1 + char2
						string = str(format(x, '02d')) + string
						check_result = check(string, data)
						if(check_result[0]):
							results[check_result[1]] = check_result[2]
		if x == 3:																# Strings of length 3
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for x in xrange(0,100):
							string = char1 + char2 + char3
							string = str(format(x, '02d')) + string
							check_result = check(string, data)
							if(check_result[0]):
								results[check_result[1]] = check_result[2]
		if x == 4:																# Strings of length 4
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for x in xrange(0,100):
								string = char1 + char2 + char3 + char4
								string = str(format(x, '02d')) + string
								check_result = check(string, data)
								if(check_result[0]):
									results[check_result[1]] = check_result[2]
	return results

def make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	size_six = 0
	size_seven = 0
	size_eight = 0

	for x in xrange(5,9):
		if x == 5:																# Strings of length 5
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for x in xrange(0,100):
									string = char1 + char2 + char3 + char4 + char5
									string = str(format(x, '02d')) + string
									check_result = check(string, data)
									if(check_result[0]):
										print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
										results[check_result[1]] = check_result[2]
		if x == 6:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for x in xrange(0,100):
										string = char1 + char2 + char3 + char4 + char5 + char6
										string = str(format(x, '02d')) + string
										check_result = check(string, data)
										if(check_result[0]):
											print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
											results[check_result[1]] = check_result[2]
		if x == 7:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for x in xrange(0,100):
											string = char1 + char2 + char3 + char4 + char5 + char6 + char7
											string = str(format(x, '02d')) + string
											check_result = check(string, data)
											if(check_result[0]):
												print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
												results[check_result[1]] = check_result[2]
		if x == 8:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for x in xrange(0,100):
												string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
												string = str(format(x, '02d')) + string
												check_result = check(string, data)
												if(check_result[0]):
													print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
													results[check_result[1]] = check_result[2]
	print "Completed strings of length 8."
	return results

def make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	results = {}

	for x in xrange(8,13):
		if x == 8:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for x in xrange(0,100):
												string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8
												string = str(format(x, '02d')) + string
												check_result = check(string, data)
												if(check_result[0]):
													print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
													results[check_result[1]] = check_result[2]

		if x == 9:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for x in xrange(0,100):
													string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9
													string = str(format(x, '02d')) + string
													check_result = check(string, data)
													if(check_result[0]):
														print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
														results[check_result[1]] = check_result[2]

		if x == 10:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													for x in xrange(0,100):
														string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10
														string = str(format(x, '02d')) + string
														check_result = check(string, data)
														if(check_result[0]):
															print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
															results[check_result[1]] = check_result[2]

		if x == 11:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													for char11 in chars:
														for x in xrange(0,100):
															string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11
															string = str(format(x, '02d')) + string
															check_result = check(string, data)
															if(check_result[0]):
																print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
																results[check_result[1]] = check_result[2]
		if x == 12:																# Strings of length 6
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									for char7 in chars:
										for char8 in chars:
											for char9 in chars:
												for char10 in chars:
													for char11 in chars:
														for char12 in chars:
															for x in xrange(0,100):
																string = char1 + char2 + char3 + char4 + char5 + char6 + char7 + char8 + char9 + char10 + char11 + char12
																string = str(format(x, '02d')) + string
																check_result = check(string, data)
																if(check_result[0]):
																	print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
																	results[check_result[1]] = check_result[2]
	print "Completed strings of length 12."
	return results

