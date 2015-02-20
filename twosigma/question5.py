#! /usr/bin/python

import csv

stocks = open('question5.csv')
csv_stocks = csv.reader(stocks)

d = {}

for row in csv_stocks:
	if row[6] != '' and row[6] != 'Volume':
		d.setdefault(row[1], []).append(int(row[6]))


for key,value in d.iteritems():
	if sum(value) > 0:
		print key + ",", sum(value)
