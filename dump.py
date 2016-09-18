#! /usr/bin/env python
import sys

def build_data(filename):
	dump_file = open(filename, "r")
	data = {}
	for line in dump_file:
		data[line[:-1]] = ""
	return data

if __name__ == '__main__':
	data = build_data(sys.argv[1])
	print data