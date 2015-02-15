#! /usr/bin/python3.4

# Pricing a European Call Option
# Paige Bailey
# Saturday, February 14, 2015

from math import *

def CND(X):
	''' Cumulative Stanard Normal Distribution'''
	(a1, a2, a3, a4, a5) = (0.31938153,-0.356563782,1.781477937,-1.821255978,1.330274429)
	L = abs(X)
	K = 1.0 / (1.0+0.2316419 * L)
	w = 1.0 - 1.0 / sqrt(2 * pi) * exp(-L * L/ 2.) * (a1 * K + a2 * K * K + a3 * pow(K, 3) + a4 * pow(K, 4) + a5 * pow(K, 5))
	if X < 0:
		w = 1.0 - w
	return w

def euro_call(S, X, T, r, sigma):
	''' 
	S = current stock price
	X = exercise price (fixed)
	T = maturity (in years)
	r = continuously compounded risk-free rate
	sigma = volatility of the underlying
	'''
		
	d1 = (log(S/X) + (r+sigma*sigma/2.0)*T) / (sigma * sqrt(T))
	d2 = d1 - sigma*sqrt(T)
	return S * CND(d1) - X*exp(-r*T) * CND(d2)



print(euro_call(40, 42, 0.5, 0.1, 0.2))

