#!/usr/bin/python

import json

def bitify(x):
	s=json.dumps(x)
	for i in bytearray(s):
		for j in range(8):
			yield i & 1
			i >>= 1

def unbitify(generator):
	result = []
	for bit_tuple in zip(*[iter(generator)] * 8):
		byte=0
		for bit in bit_tuple:
			byte >>= 1
			byte |= bit << 7
		result.append(chr(byte))
	return json.raw_decode("".join(result))

