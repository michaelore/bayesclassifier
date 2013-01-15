#!/usr/bin/env python
import csv
import re
import sys
from math import *

with open('data.csv', 'rb') as datafile:
	datareader = csv.reader(datafile)
	columns = datareader.next()
	datareader.next()
	datadict = dict()
	totals = [0 for i in xrange(0, len(columns))]
	for row in datareader:
		for i in xrange(4, len(row)):
			totals[i] += int(row[i])
		if not datadict.has_key(row[1]):
			datadict[row[1]] = row
		else:
			for i in xrange(4, len(row)):
				datadict[row[1]][i] += row[i]

evidence = map(lambda t: log(totals[4]-t+2)-log(t+2), totals)

with open('input.txt', 'rb') as inputfile:
	wordpattern = re.compile("[a-zA-Z-]+")
	def createWordGenerator():
		for line in inputfile.xreadlines():
			for word in re.findall(wordpattern, line):
				yield word
	wordgen = createWordGenerator()

	logratios = [0 for i in xrange(0, len(columns))]
	for word in wordgen:
		if datadict.has_key(word):
			tot = int(datadict[word][4])
			for i in xrange(5, len(columns)):
				count = int(datadict[word][i])
				logratios[i] += log(count+1)-log(tot-count+1)+evidence[i]

for i in xrange(5, len(columns)):
	print columns[i] + ": " + str(logratios[i])
