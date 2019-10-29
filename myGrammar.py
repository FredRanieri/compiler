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

def p_block(t):
    '''block : statement
             | statement block'''

def p_statement(t):
    '''statement : print SEMICOLON
                 | assigment SEMICOLON
                 | scan SEMICOLON
                 | if_statement'''
    t[0] = t[1]

def p_variable_name(t):
    'variable_name : VARIABLE'
    t[0] = t[1]

def p_variable_declaration(t):
    '''variable_declaration : INT variable_name
                            | FLOAT variable_name
                            | CHAR variable_name
                            | STRING variable_name'''
    t[0] = t[2]

def p_assigment(t):
    '''assigment : variable_declaration ASSINGMENT expression
                 | variable_name ASSINGMENT expression'''
    # print('t1')
    # print(t[1])
    # print('t3')
    # print(t[3])
    variables[t[1]] = t[3]

def p_print(t):
    'print : PRINT OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    print(t[3])

def p_expression(t):
    'expression : OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
    t[0] = t[2]

def p_expression_value(t):
    'expression : value'
    # print(t[1])
    t[0] = t[1]

def p_expression_variable(t):
    'expression : variable_name'
    t[0] = variables[t[1]]

def p_value_int(t):
    'value : DIGIT'
    # print(t[1])
    t[0] = int(t[1])

def p_value_float(t):
    'value : REAL'
    t[0] = float(t[1])

def p_expression_scan(t):
    'scan : SCAN OPEN_PARENTHESIS VARIABLE CLOSE_PARENTHESIS'
    variables[t[3]] = input()

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

def p_expression_not(t):
    'expression : NOT expression'
    t[0] = not t[2]

def p_expression_or(t):
    'expression : expression OR expression'
    t[0] = t[1] or t[3]

def p_expression_and(t):
    'expression : expression AND expression'
    t[0] = t[1] and t[3]

def p_expression_binop(t):
    '''expression : expression SUM expression
                  | expression SUBTRACTION expression
                  | expression MULTIPLICATION expression
                  | expression DIVISION expression
                  | expression MOD expression'''
                  
    if t[2] == '+'  : t[0] = t[1] + t[3]
    elif t[2] == '-': t[0] = t[1] - t[3]
    elif t[2] == '*': t[0] = t[1] * t[3]
    elif t[2] == '/': t[0] = t[1] / t[3]
    elif t[2] == '%': t[0] = t[1] % t[3]

def p_if_statement(t):
    'if_statement : IF OPEN_PARENTHESIS expression CLOSE_PARENTHESIS OPEN_CURLY_BRACKETS block CLOSE_CURLY_BRACKETS'
    print(t[3])
    print(t[6])
    if t[3]:
        t[0] = t[6]
    else :
        t[0]

# def p_value_char(t):
#     'value : VARIABLE'
#     print(t[2])
#     t[0] = t[2]

# def p_statement_assign(t):
#     'statement : VARIABLE ASSINGMENT expression'
#     variables[t[1]] = t[3]

# def p_statement_expr(t):
#     'statement : expression'

# def p_expression_binop(t):
#     '''expression : expression SUM expression
#                   | expression SUBTRACTION expression
#                   | expression MULTIPLICATION expression
#                   | expression DIVISION expression'''
#     if t[2] == '+'  : t[0] = t[1] + t[3]
#     elif t[2] == '-': t[0] = t[1] - t[3]
#     elif t[2] == '*': t[0] = t[1] * t[3]
#     elif t[2] == '/': t[0] = t[1] / t[3]

# '''
# def p_expression_uminus(t):
#     'expression : MINUS expression %prec UMINUS'
#     t[0] = -t[2]
# '''

# def p_expression_group(t):
#     'expression : OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
#     t[0] = t[2]

# ### Define expressao de entrada e saida

# def p_expression_scan(t):
#     'expression : SCAN OPEN_PARENTHESIS VARIABLE CLOSE_PARENTHESIS'
#     variables[t[3]] = input()

# def p_expression_print(t):
#     'expression : PRINT OPEN_PARENTHESIS expression CLOSE_PARENTHESIS'
#     print(t[3])


# ### Define expressao de tipos de variaveis

# def p_expression_int(t):
#     'expression : INT VARIABLE ASSINGMENT DIGIT'
#     variables[t[2]] = int(t[4])

# def p_expression_float(t):
#     'expression : FLOAT VARIABLE ASSINGMENT REAL'
#     variables[t[2]] = float(t[4])

# def p_expression_string(t):
#     'expression : STRING VARIABLE ASSINGMENT VARIABLE'
#     variables[t[2]] = str(t[4])

# def p_expression_char(t):
#     'expression : CHAR VARIABLE ASSINGMENT VARIABLE'
#     variables[t[2]] = t[4]

# ### Define expressao de variaveis

# def p_expression_digit(t):
#     'expression : DIGIT'
#     t[0] = t[1]

# def p_expression_real(t):
#     'expression : REAL'
#     t[0] = t[1]

# def p_expression_variable(t):
#     'expression : VARIABLE'
#     try:
#         t[0] = variables[t[1]]
#     except LookupError:
#         print("Undefined name '%s'" % t[1])
#         t[0] = 0

# ### Define expressao de operadores relacionais

# def p_expression_greater(t):
#     'expression : expression GREATER expression'
#     t[0] = (t[1] > t[3])

# def p_expression_greater_equal(t):
#     'expression : expression GREATEROREQUAL expression'
#     t[0] = (t[1] >= t[3])

# def p_expression_less(t):
#     'expression : expression LESS expression'
#     t[0] = (t[1] < t[3])

# def p_expression_less_equal(t):
#     'expression : expression LESSOREQUAL expression'
#     t[0] = (t[1] <= t[3])

# def p_expression_equal(t):
#     'expression : expression EQUAL expression'
#     t[0] = (t[1] == t[3])   

# def p_expression_different(t):
#     'expression : expression DIFFERENT expression'
#     t[0] = (t[1] != t[3])  

### Define expressao de erro

def p_error(t):
    print("Syntax error at '%s'" % t.value)

parser = yacc.yacc()

def result_parser(line):
    parser.parse(line)