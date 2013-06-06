#!/usr/bin/python
import image
import bitify
import sys

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print 'Usage: %s image.png'%(sys.argv[0])
		sys.exit(1)
	print bitify.unbitify(image.decode(sys.argv[1]))