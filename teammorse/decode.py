import StringIO


def generateLines(inputText):
	for line in StringIO.StringIO(inputText):
		if line.strip() == '':
			yield line

def decode()



