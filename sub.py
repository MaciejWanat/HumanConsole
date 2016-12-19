with open('resources/dict.tsv', 'r') as f:
    programs_names = [r.split() for r in f]

subDict = { k[0]: k[1] for k in programs_names }

def subs(string):
    if string in subDict:
        string = subDict[string]
    return string