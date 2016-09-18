import sys
def characters():
	char_file = open('characters.txt', 'r')
	chars = []
	for line in char_file:
		chars.append(line[:-1])
	return chars

def make_keywords():
	keywords = []
	chars = characters()
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
				print "Loading strings of length 1"
			for char1 in chars:
				string = char1
				keywords.append(string)
		if x == 2:																# Strings of length 2
			if size_two == 0:
				size_two = 1
				print "Completed strings of length 1"
				print "Loading strings of length 2"
			for char1 in chars:
				for char2 in chars:
					string = char1 + char2
					keywords.append(string)
		if x == 3:																# Strings of length 3
			if size_three == 0:
				size_three = 1
				print "Completed strings of length 2"
				print "Loading strings of length 3"
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						string = char1 + char2 + char3
						keywords.append(string)
		if x == 4:																# Strings of length 4
			if size_four == 0:
				size_four = 1
				print "Completed strings of length 3"
				print "Loading strings of length 4"
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							string = char1 + char2 + char3 + char4
							keywords.append(string)		
		if x == 5:																# Strings of length 5	
			if size_five == 0:
				size_five = 1
				print "Completed strings of length 4"
				print "Loading strings of length 5"
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								string = char1 + char2 + char3 + char4 + char5
								keywords.append(string)
		if x == 6:																# Strings of length 6
			if size_six == 0:
				size_six = 1
				print "Completed strings of length 5"
				print "Loading strings of length 6"
			for char1 in chars:
				for char2 in chars:
					for char3 in chars:
						for char4 in chars:
							for char5 in chars:
								for char6 in chars:
									string = char1 + char2 + char3 + char4 + char5 + char6
									keywords.append(string)	
	return keywords

if __name__ == '__main__':
	keywords = make_keywords()
	print keywords
	print data