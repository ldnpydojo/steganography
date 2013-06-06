import string

WHITESPACE_TO_NUMERALS = {'\t':'1', ' ':'0'}
NUMERALS_TO_WHITESPACE = dict((v,k) for k,v in WHITESPACE_TO_NUMERALS.items())

LETTERS = string.lowercase + ' '
