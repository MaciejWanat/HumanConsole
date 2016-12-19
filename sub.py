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
    'worda' : 'msword',
    'excel' : 'EXCEL',
    'excela' : 'EXCEL',
    'access' : 'msaccess',
    'accessa' : 'msaccess',
    'filezille' : 'filezilla',
    'skype' : 'Skype',
    'skajpa' : 'Skype',
    'skajp' : 'Skype',
    'steam' : 'Steam',
    'steama' : 'Steam'
}

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string