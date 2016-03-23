# -*- coding: utf-8 -*-
import ply.yacc as yacc
from lex import tokens

def p_italics(p):
	'exp :  TIMES TEXT TIMES'
	p[0] = '<em>{}</em>'.format(p[2])
	
def p_strong(p):
	'exp :  TIMES TIMES TEXT TIMES TIMES'
	p[0] = '<strong>'+p[3]+'</strong>'

def p_italicsStrong(p):
	'exp :  TIMES TIMES TIMES TEXT TIMES TIMES TIMES'
	p[0] = '<strong><em>'+p[4]+'</em></strong>'

def p_titleOne(p):
	'exp : NUMBERSIGN TEXT	'
	p[0] = '<h1>'+p[2]+'<h1>'


#def p_title2(p):
#	'exp : NUMBERSIGN NUMBERSIGN TEXT'
#	p[0] = '<h2>'+p[3]+'<h2>'

#def p_title3(p):
#	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
#	p[0] = '<h3>'+p[4]+'<h3>'
	
#def p_title4(p):
#	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
#	p[0] = '<h4>'+p[5]+'<h4>'
	
#def p_title5(p):
#	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
#	p[0] = '<h5>'+p[6]+'<h5>'

#def p_title6(p):
#	'exp : NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN NUMBERSIGN TEXT'
#	p[0] = '<h6>'+p[7]+'<h6>'
	
#def p_image(p):
#	'exp	 : EXCLAMATIONM LBRACKET TEXT RBRACKET LPAREN TEXT COLON TEXT RPAREN'
#	p[0] = '<img src="' + p[6] + p[7] + p[8] +'" alt="' + p[3] + '">'

#def p_blockquotes(p):
#	'exp : GREATERTHAN TEXT'
#	p[0] = '<blockquote>'+ p[2]+'</blockquote>'
	
#def p_factor_num(p):
#	'gta : NUMBERSIGN'
#	p[0] = p[1]

def p_empty(p):
    'empty :'
    pass
    
def p_error(p):
    print p
    if p is not None:
        print "Syntax error at line " + str(p.lexer.lineno) + " Unexpected token  " + str(p.value)
    else:
        print "Syntax error at line: " + str(cminus_lexer.lexer.lineno) 
parser = yacc.yacc()
