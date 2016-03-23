# -*- coding: utf-8 -*-
import sys, os
import ply.yacc as yacc
from yacc1 import parser

def readFile(name):
	print name
	f = open(name, 'r')
	text = f.read()
	print text
	return text
	
		
def writeFile(text):
	
	wfile = open('tmp/index.html', 'w')
	wfile.write('<!DOCTYPE HTML>\n')	
	wfile.write('<html>\n')
	wfile.write('\t<head>\n')
	wfile.write('\t\t<title>Escribano </title>\n')
	wfile.write('\t</head>\n')
	wfile.write('\t<body>\n')
	wfile.write('\t\t'+str(text))
	print text
	wfile.write('\n\t</body>\n')
	wfile.write('</html>\n')


def main():

	textMarkdown = parser.parse(readFile('tmp/'+'index.md'))
	writeFile(textMarkdown)
	
	
if __name__ == '__main__':
	
	main()

