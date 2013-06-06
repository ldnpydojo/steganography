import unittest
from decode import convert
from constants import LETTERS, NUMERALS_TO_WHITESPACE

class TestDecode(unittest.TestCase):

	@staticmethod
	def to_whitespace(letter):
		return "".join(NUMERALS_TO_WHITESPACE[b] for b in bin(LETTERS.index(letter))[2:])

	def test_convert(self):
		self.assertEqual(convert(self.to_whitespace('a')), 'a')

	

if __name__ == '__main__':
	unittest.main()