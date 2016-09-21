#! /usr/bin/env python

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

def common_passwords(PASSWORD_FILE):
	password_file = open(PASSWORD_FILE, 'r')
	passwords = []
	for line in password_file:
		line = line[:-1]
		passwords.append(line)
		passwords.append(line.upper())
	return passwords

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

def print_out(OUTPUT_FILENAME, PASSWORD, HASH):
	out_file = open(OUTPUT_FILENAME, "a")
	out_file.write("%s : %s\n" % (PASSWORD, HASH))
	out_file.close()

# PASSWORD + Strings of length 1 - 3
def make_keywords_1(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	passwords = common_passwords(PASSWORD_FILE)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			for password in passwords:
				for x in xrange(0,100):
					for char1 in chars:
						string = str(format(x, '02d')) + password + char1
						check_result = check(string, data)
						if(check_result[0]):
							print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
							results[check_result[1]] = check_result[2]
		if x == 2:																# Strings of length 2
			for password in passwords:
				for x in xrange(0,100):
					for char1 in chars:
						for char2 in chars:
							string = str(format(x, '02d')) + password + char1 + char2
							check_result = check(string, data)
							if(check_result[0]):
								print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
								results[check_result[1]] = check_result[2]
		if x == 3:																# Strings of length 3
			for password in passwords:	
				for x in xrange(0,100):
					for char1 in chars:
						for char2 in chars:
							for char3 in chars:
								string = str(format(x, '02d')) + password + char1 + char2 + char3
								check_result = check(string, data)
								if(check_result[0]):
									print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
									results[check_result[1]] = check_result[2]
	return results

def make_keywords_2(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	passwords = common_passwords(PASSWORD_FILE)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			for password in passwords:
				for x in xrange(0,100):
					for char1 in chars:
						string = str(format(x, '02d')) + char1 + password
						check_result = check(string, data)
						if(check_result[0]):
							print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
							results[check_result[1]] = check_result[2]

		if x == 2:																# Strings of length 2
			for password in passwords:
				for x in xrange(0,100):
					for char1 in chars:
						for char2 in chars:
							string = str(format(x, '02d')) + char1 + char2 + password
							check_result = check(string, data)
							if(check_result[0]):
								print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
								results[check_result[1]] = check_result[2]
		if x == 3:																# Strings of length 3
			for password in passwords:	
				for x in xrange(0,100):
					for char1 in chars:
						for char2 in chars:
							for char3 in chars:
								string = str(format(x, '02d')) + char1 + char2 + char3 + password 
								check_result = check(string, data)
								if(check_result[0]):
									print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
									results[check_result[1]] = check_result[2]
	return results

'''def make_keywords_3(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	passwords = common_passwords(PASSWORD_FILE)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			if size_one == 0:
				size_one = 1
				print "Trying strings of length 1..."
			for password in passwords:
				for char1 in chars:
					string = password + char1
					check_result = check(string, data)
					if(check_result[0]):
						print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
						results[check_result[1]] = check_result[2]
		if x == 2:																# Strings of length 2
			if size_two == 0:
				size_two = 1
				print "Completed strings of length 1."
				print "Trying strings of length 2..."
			for password in passwords:
				for char1 in chars:
					for char2 in chars:
						string = password + char1 + char2
						check_result = check(string, data)
						if(check_result[0]):
							print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
							results[check_result[1]] = check_result[2]
		if x == 3:																# Strings of length 3
			if size_three == 0:
				size_three = 1
				print "Completed strings of length 2."
				print "Trying strings of length 3..."
			for password in passwords:	
				for char1 in chars:
					for char2 in chars:
						for char3 in chars:
							string = password + char1 + char2 + char3
							check_result = check(string, data)
							if(check_result[0]):
								print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
								results[check_result[1]] = check_result[2]
		if x == 4:																# Strings of length 4
			if size_four == 0:
				size_four = 1
				print "Completed strings of length 3."
				print "Trying strings of length 4..."
			for password in passwords:
				for char1 in chars:
					for char2 in chars:
						for char3 in chars:
							for char4 in chars:
								string = password + char1 + char2 + char3 + char4
								check_result = check(string, data)
								if(check_result[0]):
									print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
									results[check_result[1]] = check_result[2]
	print "Completed strings of length 4."
	return results

def make_keywords_4(HASH_FILENAME, CHARACTERS_FILENAME, OUTPUT_FILENAME, PASSWORD_FILE):
	data = build_data(HASH_FILENAME)
	keywords = []
	chars = characters(CHARACTERS_FILENAME)

	passwords = common_passwords(PASSWORD_FILE)

	results = {}

	size_one = 0
	size_two = 0
	size_three = 0
	size_four = 0
	size_five = 0
	size_six = 0

	for x in xrange(1,6):
		if x == 1:																# Strings of length 1
			if size_one == 0:
				size_one = 1
				print "Trying strings of length 1..."
			for password in passwords:
				for char1 in chars:
					string = char1 + password
					check_result = check(string, data)
					if(check_result[0]):
						print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
						results[check_result[1]] = check_result[2]
		if x == 2:																# Strings of length 2
			if size_two == 0:
				size_two = 1
				print "Completed strings of length 1."
				print "Trying strings of length 2..."
			for password in passwords:
				for char1 in chars:
					for char2 in chars:
						string = char1 + char2 + password
						check_result = check(string, data)
						if(check_result[0]):
							print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
							results[check_result[1]] = check_result[2]
		if x == 3:																# Strings of length 3
			if size_three == 0:
				size_three = 1
				print "Completed strings of length 2."
				print "Trying strings of length 3..."
			for password in passwords:	
				for char1 in chars:
					for char2 in chars:
						for char3 in chars:
							string = char1 + char2 + char3 + password
							check_result = check(string, data)
							if(check_result[0]):
								print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
								results[check_result[1]] = check_result[2]
		if x == 4:																# Strings of length 4
			if size_four == 0:
				size_four = 1
				print "Completed strings of length 3."
				print "Trying strings of length 4..."
			for password in passwords:
				for char1 in chars:
					for char2 in chars:
						for char3 in chars:
							for char4 in chars:
								string = char1 + char2 + char3 + char4 + password 
								check_result = check(string, data)
								if(check_result[0]):
									print_out(OUTPUT_FILENAME, check_result[1], check_result[2])
									results[check_result[1]] = check_result[2]
	print "Completed strings of length 4."
	return results'''