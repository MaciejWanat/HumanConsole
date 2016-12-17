import os
import re
import webbrowser
from sub import subs

#WINDOWS VER

tokens = (
    'OPEN', 'PATH', 'CLOSE' , 'AND'
)

# Tokens

t_AND = r'(i|oraz)'
t_CLOSE = r'(zamknij|zako[nń]cz|zamkn[ąa][cć]|zako[nń]czy[cć])'
t_OPEN = r'(otw[oó]rz|uruchom|otw[oó]rzy[cć]|uruchomi[cć])'
t_PATH = r'(?!(i|oraz|zamknij|zako[nń]cz|zamkn[ąa][cć]|zako[nń]czy[cć]|otw[oó]rz|uruchom|otw[oó]rzy[cć]|uruchomi[cć])\b)\b(\S+)\b' #match everything except for the beggining words

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
    searchwww = re.search('www\.', t)
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
    os.system("taskkill /IM " + t + ".exe" + " >nul")
    return

# parser

#single
def p_statement_open(t):
    'statement : OPEN PATH'
    print("Otwieram " + t[2])
    onWWW(t[2])

def p_statement_close(t):
    'statement : CLOSE PATH'
    print("Zamykam program " + t[2])
    cExe(t[2])

#multiple
def p_statement_open_m(t):
    'statement : OPEN PATH AND PATH'
    print("Otwieram " + t[2] + " oraz " + t[4])
    onWWW(t[2])
    onWWW(t[4])

def p_statement_close_m(t):
    'statement : CLOSE PATH AND PATH'
    print("Zamykam program " + t[2] + " oraz program "+ t[4])
    cExe(t[2])
    cExe(t[4])

def p_error(t):
    pass

import ply.yacc as yacc
parser = yacc.yacc()

while True:
    try:
        s = input('humanConsole > ')   # Use raw_input on Python 2
    except EOFError:
        break
    parser.parse(s)
