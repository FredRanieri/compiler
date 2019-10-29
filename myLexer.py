#!/usr/local/bin/env python3

from ply import *

reserved_words = {
    # Tipos de variaveis
    'int' : 'INT',
    'float' : 'FLOAT',
    'char' : 'CHAR',
    'string' : 'STRING',

    # Comandos de entrada e saida
    'scan' : 'SCAN',
    'print' : 'PRINT',

    # Comandos condicionais
    'if': 'IF',
    'elif' : 'ELIF',
    'else': 'ELSE',

    # Comandos de repetição
    'while': 'WHILE',
    'for': 'FOR',

    # Estrutura para função
    'func': 'FUNC',
    'return': 'RETURN',

    # Operadores lógicos
    'and' : 'AND',
    'or' : 'OR',
}

tokens = [
    # Operador de atribuição
    'ASSINGMENT',

    # Operadores relacionais
    'EQUAL',
    'DIFFERENT',
    'GREATER',
    'GREATEROREQUAL',
    'LESS',
    'LESSOREQUAL',
    'NOT',

    # Operadores aritméticos
    'SUM',
    'SUBTRACTION',
    'MULTIPLICATION',
    'DIVISION',
    'MOD',

    # Simbolos especiais
    'OPEN_PARENTHESIS',
    'CLOSE_PARENTHESIS',
    'SINGLE_QUOTATION_MARK',
    'QUOTATION_MARKS',
    'PERIOD',
    'COMMA',
    'COLON',
    'SEMICOLON',
    'OPEN_SQUARE_BRACKETS',
    'CLOSE_SQUARE_BRACKETS',

    # Blocos de comando
    'OPEN_CURLY_BRACKETS',
    'CLOSE_CURLY_BRACKETS',

    # Numeros e letras
    'DIGIT',
    'REAL',
    'VARIABLE',
    'CHARACTER',
    'WORD',
    'EMPTY'
] + list(reserved_words.values())

# Operador de atribuição
t_ASSINGMENT             =   r"="

# Operadores relacionais
t_EQUAL                  =   r"=="
t_DIFFERENT              =   r"!="
t_GREATER                =   r">"
t_GREATEROREQUAL         =   r">="
t_LESS                   =   r"<"
t_LESSOREQUAL            =   r"<="
t_NOT                    =   r"!"

# Operadores aritméticos
t_SUM                    =   r"\+"
t_SUBTRACTION            =   r"-"
t_MULTIPLICATION         =   r"\*"
t_DIVISION               =   r"/"
t_MOD                    =   r"%"

# Simbolos especiais
t_OPEN_PARENTHESIS       =   r"\("
t_CLOSE_PARENTHESIS      =   r"\)"
t_SINGLE_QUOTATION_MARK  =   r"\'"
t_QUOTATION_MARKS        =   r"\”"
t_PERIOD                 =   r"\."
t_COMMA                  =   r","
t_COLON                  =   r":"
t_SEMICOLON              =   r";"
t_OPEN_SQUARE_BRACKETS   =   r"\["
t_CLOSE_SQUARE_BRACKETS  =   r"\]"

# Blocos de comando
t_OPEN_CURLY_BRACKETS    =   r"\{"
t_CLOSE_CURLY_BRACKETS   =   r"\}"
# t_CHARACTER              =   r'[\'][a-zA-Z][\']'

def t_REAL(t):
    r'\d+[eE][-+]?\d+|(\.\d+|\d+\.\d+)([eE][-+]?\d+)?'
    t.value = float(t.value)
    return t

def t_DIGIT(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# def t_WORD(t):
#     r'["][a-z A-Z_0-9]*["]'
#     return t

# def t_CHARACTER(t):
#     r'[\'][a-zA-Z][\']'
#     return t

def t_VARIABLE(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    if t.value in reserved_words:
        t.type = reserved_words[t.value]
    return t

def t_IGNORE(t):
    r'[ \n\t\"\']'

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")

def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)

lexer = lex.lex()

def create_token_table(lines):
    token_table = []
    for line in lines:
        lexer.input(line)
        while True:
            token = lexer.token()
            if not token:
                break
            token_table.append(token)
            print(token)

    return token_table