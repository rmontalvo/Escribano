from yacc1 import parser

def readFile(name):
	print name
	f = open(name, 'r')
	text = f.read()
	print text
	return text
    
def test_list():
	textMarkdown = p
	assert parser.parse(readFile('tmp/index.md')) == readFile('tmp/index.htmls') 
