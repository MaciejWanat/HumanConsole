import os
import re
import webbrowser
from sub import subs

#WINDOWS VER

tokens = (
    'OPEN', 'PATH', 'CLOSE'
)

# Tokens

t_CLOSE = r'(end|finish)'
t_OPEN = r'(open|start|run)'
t_PATH = r'(?!(open|start|run|end|finish)\b)\b(\S+)\b' #match everything except for the beggining words

def t_error(t):
    t.lexer.skip(1)

# Ignored characters
t_ignore = " \t"

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# parser

def p_statement_open(t):
    'statement : OPEN PATH'
    print("Opening " + t[2])
#    t[2] = subs(t[2]) polish names
    searchwww = re.search('www\.', t[2])
    if not searchwww:
        os.system("start "+ t[2])
    else:
        webbrowser.open(t[2])

def p_statement_close(t):
    'statement : CLOSE PATH'
    print("Closing program " + t[2])
    searchexe = re.search ('\.exe', t[2])
    if not searchexe:
        os.system("taskkill /IM " + t[2] + ".exe" + " >nul")
#        cmd = subs(t[2])   # for polish
    else:
        os.system("taskkill /IM " + t[2] + " >nul")
#        cmd = subs(t[2][:3]) # for polish

def p_error(t):
    print("I didn't understand your command!")

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('humanConsole > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
