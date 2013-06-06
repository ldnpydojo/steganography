import sys
from constants import WHITESPACE_TO_NUMERALS
from constants import LETTERS

def generateLines(inputFile):
	for line in inputFile:
		if line.strip() == '':
			yield line.strip('\r\n')

def convert(inputLine):
	binaryChars = []
	for char in inputLine:
		binaryChars.append(WHITESPACE_TO_NUMERALS[char])

	charString = ''.join(binaryChars)
	hiddenNumber = int(charString, 2)
	return LETTERS[hiddenNumber]

def generateLetters(inputText):
	for line in generateLines(inputText):
		yield convert(line)

def decode(inputFile):
	return ''.join(generateLetters(inputFile))

if __name__ == '__main__':
	inputFileName = sys.argv[1]
	with open(inputFileName) as inputFile:
		print(decode(inputFile))