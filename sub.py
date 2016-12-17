subDict = {
    'notatnik' : 'notepad',
    'word' : 'winword',
    'internet explorer' : 'iexplore',
    'internetexplorer' : 'iexplore',
    'wiersz polecenia' : 'cmd'
}

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string