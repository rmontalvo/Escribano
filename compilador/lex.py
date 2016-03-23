# -*- coding: utf-8 -*-
import os
import sys
from ply import lex

tokens = (
	'TEXT', 
	'PLUS',
	'MINUS',
	'TIMES',
	'EQUAL',
	'COLON',
	'COMMA',
	'DIVIDE',
	'ATSIGN',
	'LPAREN',
	'RPAREN',
	'LBLOCK',
	'RBLOCK',
	'LBRACKET',
	'RBRACKET',
	'SEMICOLON',
	'DOLARSIGN',
	'NUMBERSIGN',
	'GREATERTHAN',
	'EXCLAMATIONM',
	'IEXCLAMATIONM',
	'NUMBER',
	'ELSE',
)

reserved = {
	'nil' : 'NIL',
}

t_TEXT = r'[a-zA-Z_][\w_]*'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_EQUAL  = r'='
t_COLON = r'\.'
t_COMMA = ','
t_DIVIDE = r'\/'
t_ATSIGN = r'\@'
t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBLOCK   = r'{'
t_RBLOCK   = r'}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_DOLARSIGN = r'\$'
t_NUMBERSIGN = r'\#'
t_GREATERTHAN = r'\>'
t_EXCLAMATIONM = r'\!'
t_IEXCLAMATIONM = r'\¡'
t_ignore = ' '
#t_ignore_NEWLINE = r'[\r\t\v\]+'
t_SEMICOLON = r';'
#t_ignore = r'\t\x0c'
#t_ignore  = ' '

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    print 'Valor [t]:  = '
    print t.value
    return t

def t_newline(t):
	r'\n+'
	t.lexer.lineno += t.value.count('\n')
	
def t_error(t):
	message = 'Token desconocido'
	message = '\type: ' + token.type
	message = '\nValue: ' + str(token.value)
	message = '\line: ' + str(token.lineo)
	message = '\nposition: ' + str(token.lexpos)
	raise Exception(message)

def t_ELSE(t):
    r'else'
    return t
    
lex.lex()
inp = open('tmp/index.md','r')
lex.input(inp.read())

for tok in iter(lex.token, None):
	print tok
	#~ print repr(tok.type),repr(tok.value)
	#~ print repr(tok.lexpos)
