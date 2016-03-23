import os, sys, yacc
from lex import tokens


def p_expression_title(subexpr):
	'expresion: NUMBERSIGN VAR term'
	subexpr[0] = add(subexpr[1], subexpr[3])


def p_error(tokens):
	raise Exceptionn("Syntax error")
