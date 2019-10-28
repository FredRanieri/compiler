#!/usr/local/bin/env python3

import ply.yacc as yacc
from myLexer import tokens

precedence = (
    ('left','SUM','SUBTRACTION'),
    ('left','MULTIPLICATION','DIVISION'),
    ('nonassoc', 'GREATER', 'GREATEROREQUAL', 'LESS', 'LESSOREQUAL', 'EQUAL', 'DIFFERENT'),
    #('right','UMINUS'),
    )

variables = { }

### Atribui o resultado de uma expressão na variavel

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

### Define expressao de entrada e saida

def p_expression_scan(t):
    'expression : SCAN OPEN_PARENTHESIS VARIABLE CLOSE_PARENTHESIS'
    variables[t[3]] = input()

def p_expression_print(t):
    'expression : PRINT OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    print(t[3])


### Define expressao de tipos de variaveis

def p_expression_int(t):
    'expression : INT VARIABLE ASSINGMENT DIGIT'
    variables[t[2]] = int(t[4])

def p_expression_float(t):
    'expression : FLOAT VARIABLE ASSINGMENT REAL'
    variables[t[2]] = float(t[4])

def p_expression_string(t):
    'expression : STRING VARIABLE ASSINGMENT VARIABLE'
    variables[t[2]] = str(t[4])

def p_expression_char(t):
    'expression : CHAR VARIABLE ASSINGMENT VARIABLE'
    variables[t[2]] = t[4]

### Define expressao de variaveis

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

### Define expressao de operadores relacionais

def p_expression_greater(t):
    'expression : expression GREATER expression'
    t[0] = (t[1] > t[3])

def p_expression_greater_equal(t):
    'expression : expression GREATEROREQUAL expression'
    t[0] = (t[1] >= t[3])

def p_expression_less(t):
    'expression : expression LESS expression'
    t[0] = (t[1] < t[3])

def p_expression_less_equal(t):
    'expression : expression LESSOREQUAL expression'
    t[0] = (t[1] <= t[3])

def p_expression_equal(t):
    'expression : expression EQUAL expression'
    t[0] = (t[1] == t[3])   

def p_expression_different(t):
    'expression : expression DIFFERENT expression'
    t[0] = (t[1] != t[3])  

### Define expressao de erro

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

def result_parser(line):
    parser.parse(line)