#!/usr/bin/env python
# 

import sys
import constants

def encode(c):
    try:
        val = constants.LETTERS.index(c)
        val = bin(val)[2:]
        result = ''
        for i in val:
            result += constants.NUMERALS_TO_WHITESPACE[i]
        return result
    except:
        return ''

def run(filename):

    with open(filename, 'r') as f:
        host_text = f.readlines()

    host_text_iter = iter(host_text)
    out_lines =[]
    for line in sys.stdin.readline():
        for next_char in line:
            for text_line in host_text_iter:
                if not text_line.strip():
                    out_lines.append(encode(next_char) + '\n')
                    break
                else:
                    out_lines.append(text_line)


    with open('out.txt', 'w') as f:
        f.write(''.join(out_lines))
        f.write(''.join(host_text_iter))



if __name__ == '__main__':
    import sys
    run(sys.argv[1])
