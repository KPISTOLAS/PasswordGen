import random

Num = ['0','1','2','3','4','5','6','7','8','9']
UL = [chr(i) for i in range(65, 91)]
LL = [chr(i) for i in range(97, 123)]
Sym = [
    '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
    '-', '_', '=', '+', '[', ']', '{', '}', '|', '\\',
    ';', ':', ',', '.', '<', '>', '/', '?', '`', '~',
    "'", '"'
]

def create():
    length = 16
    res = ""
    for i in range(length):
        if i % 2 == 0:
            t = random.randint(0, len(Num) - 1)
            res += Num[t]
        elif i % 3 == 0:
            t = random.randint(0, len(UL) - 1)
            res += UL[t]
        elif i % 4 == 0:
            t = random.randint(0, len(LL) - 1)
            res += LL[t]
        else:
            t = random.randint(0, len(Sym) - 1)
            res += Sym[t]        
    return res

x = create()
print("Your password is: " + x)
