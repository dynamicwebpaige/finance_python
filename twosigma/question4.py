#! /usr/bin/python

import csv

stocks = open('question4.csv')
csv_stocks = csv.reader(stocks)

asks = []
bids = []

for row in csv_stocks:
	if row[4] == "Quote":
		if row[1] == "07-APR-2014":
			asks.append(float(row[9]))
			bids.append(float(row[7]))

print "%.2f" % min(asks) , "\n" , "%.2f" % max(bids)





