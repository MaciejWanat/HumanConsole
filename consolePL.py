import os
import re
import webbrowser
from sub import subs
import linecache

#WINDOWS VER

tokens = (
    'OPEN', 'PATH', 'CLOSE' , 'AND'
)

# Tokens
t_AND = r'\b(' + re.sub(' ','|',linecache.getline('resources/regex.txt', 1)[:-1]) + r')\b'
t_CLOSE = r'\b(' + re.sub(' ','|',linecache.getline('resources/regex.txt', 2)[:-1]) + r')\b'
t_OPEN = r'\b(' + re.sub(' ','|',linecache.getline('resources/regex.txt', 3)[:-1]) + r')\b'
t_PATH = r'\b(' + re.sub(' ','|',linecache.getline('resources/regex.txt', 4)[:-1]) + r')\b'
#t_PATH = r'\b(' + re.sub(' ','|',linecache.getline('regex.txt', 5)[:-1]) + r')\b' another approach


def t_error(t):
    t.lexer.skip(1)

# Ignored characters
t_ignore = " \t"

# Build the lexer
import ply.lex as lex
lexer = lex.lex()

# funkcje otwierające/zamykające
def onWWW(t):
    t = subs(t)
    searchwww = re.search(r'(www\.|http|\.pl|\.com)', t)
    if not searchwww:
        os.system("start " + t)
    else:
        webbrowser.open(t)
    return

def cExe(t):
    searchexe = re.search ('\.exe', t)
    if not searchexe:
        t = subs(t)
    else:
        t = subs(t[:3])
    os.system("taskkill /F /IM " + t + ".exe" + " >nul")
    return

# parser

#single
def p_statement_open(t):
    'expression : OPEN PATH'
    print("Otwieram " + t[2])
    onWWW(t[2])

def p_statement_close(t):
    'expression : CLOSE PATH'
    print("Zamykam " + t[2])
    cExe(t[2])

#multiple
def p_statement_open_m(t):
    'expression : OPEN PATH AND PATH'
    print("Otwieram " + t[2] + " oraz " + t[4])
    onWWW(t[2])
    onWWW(t[4])

def p_statement_close_m(t):
    'expression : CLOSE PATH AND PATH'
    print("Zamykam " + t[2] + " oraz "+ t[4])
    cExe(t[2])
    cExe(t[4])

def p_error(t):
    print('Nieznana składnia')

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('humanConsole > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s.lower())
