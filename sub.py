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
    'painta' : 'mspaint',
    'worda' : 'word',
    'excela' : 'excel',
    'access' : 'msaccess',
    'accessa' : 'msaccess'
}

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string