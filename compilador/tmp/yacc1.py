# -*- coding: utf-8 -*-
import ply.yacc as yacc
from lex import tokens

def p_italics(p):
	'exp :  TIMES TEXT TIMES'
	p[0] = '<em>'+p[2]+'</em>'
	
def p_strong(p):
	'exp :  TIMES TIMES TEXT TIMES TIMES'
	p[0] = '<strong>'+p[3]+'</strong>'

def p_italicsStrong(p):
	'exp :  TIMES TIMES TIMES TEXT TIMES TIMES TIMES'
	p[0] = '<strong><em>'+p[4]+'</em></strong>'

def p_title1(p):
	'exp : NUMBERSIGN TEXT'
	p[0] = '<h1>'+p[2]+'<h1>'

def p_title2(p):
	'exp : NUMBERSIGN NUMBERSIGN TEXT'
	p[0] = '<h2>'+p[3]+'<h2>'

def p_title3(p):
	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
	p[0] = '<h3>'+p[4]+'<h3>'
	
def p_title4(p):
	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
	p[0] = '<h4>'+p[5]+'<h4>'
	
def p_title5(p):
	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
	p[0] = '<h5>'+p[6]+'<h5>'

def p_title6(p):
	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
	p[0] = '<h6>'+p[7]+'<h6>'
	
def p_image(p):
	'exp	 : EXCLAMATIONM LBRACKET TEXT RBRACKET LPAREN TEXT POINT TEXT RPAREN'
	p[0] = '<img src="' + p[6] + p[7] + p[8] +'" alt="' + p[3] + '">'

def p_blockquotes(p):
	'exp : GREATERTHAN TEXT'
	p[0] = '<blockquote>'+ p[2]+'</blockquote>'
	

def p_expression_plus(p):
	'expression : expression PLUS term'
	p[0] = p[1] + p[3]

def p_expression_minus(p):
	'expression : expression MINUS term'
	p[0] = p[1] - p[3]

def p_expression_term(p):
	'expression : term'
	p[0] = p[1]

def p_term_times(p):
	'term : term TIMES factor'
	p[0] = p[1] * p[3]

def p_term_div(p):
	'term : term DIVIDE factor'
	p[0] = p[1] / p[3]

def p_term_factor(p):
	'term : factor'
	p[0] = p[1]

def p_factor_num(p):
	'factor : NUMBER'
	p[0] = p[1]

def p_factor_expr(p):
	'factor : LPAREN expression RPAREN'
	p[0] = p[2]

def p_empty(p):
	'empty : '
	pass

def p_error(p):
	print("Syntax error in input!")
	
parser = yacc.yacc()
