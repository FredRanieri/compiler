#!/usr/local/bin/env python3

import sys
import myLexer

extention = '.qmn'

def main():
    file_name = sys.argv[1]
    token_table = []

    if file_name[-4:] != extention:
        print('fail: Erro com a extenção do arquivo.')
        exit(1)

    with open(file_name, 'r') as file:
        token_table = myLexer.create_token_table(file.readlines())

    for t in token_table:
        print(t)

if __name__ == "__main__":
    main()
