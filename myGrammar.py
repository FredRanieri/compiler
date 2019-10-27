#!/usr/local/bin/env python3

import ply.yacc as yacc
from myLexer import tokens

precedence = (
    ('left','SUM','SUBTRACTION'),
    ('left','MULTIPLICATION','DIVISION'),
    #('right','UMINUS'),
    )

variables = { }

# Atribui o resultado de uma expressão na variavel
def p_statement_assign(t):
    'statement : VARIABLE ASSINGMENT expression'
    variables[t[1]] = t[3]

def p_statement_expr(t):
    'statement : expression'
    print(t[1])

def p_expression_binop(t):
    '''expression : expression SUM expression
                  | expression SUBTRACTION expression
                  | expression MULTIPLICATION expression
                  | expression DIVISION expression'''
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]

'''
def p_expression_uminus(t):
    'expression : MINUS expression %prec UMINUS'
    t[0] = -t[2]
'''

def p_expression_group(t):
    'expression : OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    t[0] = t[2]

def p_expression_digit(t):
    'expression : DIGIT'
    t[0] = t[1]

def p_expression_variable(t):
    'expression : VARIABLE'
    try:
        t[0] = variables[t[1]]
    except LookupError:
        print("Undefined name '%s'" % t[1])
        t[0] = 0

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

def result_parser(line):
    print(parser.parse(line))