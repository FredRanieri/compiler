#!/usr/local/bin/env python3

import sys
import myLexer
import myGrammar

extention = '.qmn'

def main():
    file_name = sys.argv[1]
    token_table = []

    if file_name[-4:] != extention:
        print('fail: Erro com a extenção do arquivo.')
        exit(1)

    with open(file_name, 'r') as file:
        lines = file.readlines()
        token_table = myLexer.create_token_table(lines)

        for line in ''.join(lines).split(';'):
            if len(line) != 0:
                myGrammar.result_parser(line)

if __name__ == "__main__":
    main()
