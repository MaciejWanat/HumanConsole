subDict = {
    'notatnik' : 'notepad',
    'word' : 'winword',
    'internet explorer' : 'iexplore',
    'internetexplorer' : 'iexplore',
    'wiersz polecenia' : 'cmd',
    'wiersz polecen' : 'cmd',
    'wiersz poleceń' : 'cmd',
    'sublime text' : 'sublime_text',
    'paint' : 'mspaint',
}

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string