import unittest
from StringIO import StringIO
from decode import convert, decode
from constants import LETTERS, NUMERALS_TO_WHITESPACE

class TestDecode(unittest.TestCase):

	@staticmethod
	def to_whitespace(letter):
		return "".join(NUMERALS_TO_WHITESPACE[b] for b in bin(LETTERS.index(letter))[2:])

	@classmethod
	def words_to_whitespace(cls, letters):
		return "\n".join(cls.to_whitespace(l) for l in letters)

	def test_convert(self):
		self.assertEqual(convert(self.to_whitespace('a')), 'a')
	
	def testDecode(self):
		clearText = 'the quick vsjdjshsd'
		whitespace = self.words_to_whitespace(clearText)
		self.assertEquals(decode(StringIO(whitespace)), clearText)


if __name__ == '__main__':
	unittest.main()