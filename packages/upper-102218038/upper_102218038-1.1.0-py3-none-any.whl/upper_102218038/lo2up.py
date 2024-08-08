lo2up = {
    'a':'A',
    'b':'B',
    'c':'C',
    'd':'D',
    'e':"E",
    'f':'F',
    'g':'G',
    'h':'H',
    'i':'I',
    'j':'J',
    'k':'K',
    'l':'L',
    'm':'M',
    'n':'N',
    'o':'O',
    'p':'P',
    'q':'Q',
    'r':'R',
    's':'S',
    't':'T',
    'u':'U',
    'v':'V',
    'w':'W',
    'x':"X",
    'y':'Y',
    'z':'Z'
}
k = lo2up.keys
def up(s):
    for i in range(len(s)):
        if s[i] in k:
            s[i] = lo2up[s[i]]
    return s