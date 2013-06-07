#!/usr/bin/python
import image
import bitify
import sys

def main(input,output):
	image.encode(input, bitify.bitify(sys.stdin.read()) , output)

if __name__ == '__main__':
	if len(sys.argv) != 3 or not sys.argv[2].endswith('.png'):
		print 'Usage: %s image.jpg output.png'%(sys.argv[0])
		sys.exit(1)
	main(sys.argv[1],sys.argv[2])