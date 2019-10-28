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

def p_expression_scan(t):
    'expression : SCAN OPEN_PARENTHESIS VARIABLE CLOSE_PARENTHESIS'
    variables[t[3]] = input()

def p_expression_print(t):
    'expression : PRINT OPEN_PARENTHESIS VARIABLE CLOSE_PARENTHESIS'
    print(variables[t[3]])

def p_expression_int(t):
    'expression : INT VARIABLE ASSINGMENT DIGIT'
    variables[t[2]] = int(t[4])

def p_expression_float(t):
    'expression : FLOAT VARIABLE ASSINGMENT REAL'
    variables[t[2]] = float(t[4])

def p_expression_string(t):
    'expression : STRING VARIABLE ASSINGMENT QUOTATION_MARKS VARIABLE QUOTATION_MARKS'
    variables[t[2]] = str(t[5])

def p_expression_char(t):
    'expression : CHAR VARIABLE ASSINGMENT SINGLE_QUOTATION_MARK VARIABLE SINGLE_QUOTATION_MARK'
    variables[t[2]] = t[5]

def p_expression_digit(t):
    'expression : DIGIT'
    t[0] = t[1]

def p_expression_real(t):
    'expression : REAL'
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
    parser.parse(line)