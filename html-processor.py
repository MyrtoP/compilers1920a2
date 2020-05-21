# Eisagogi biblio8ikis
import re


def function(m):
    if (m.group(0) == '&amp;'):
        return '&'
    elif (m.group(0) == '&gt;'):
        return '>'
    elif (m.group(0) == '&lt;'):
        return '<'
    elif (m.group(0) == '&nbsp;'):
        return ' '


# Erotimata
# ejagogi & ektiposi titlou
rexp = re.compile('<title>(.+)</title>', re.DOTALL)
# Apalifi sxolion
rexp1 = re.compile('<!--.+?-->', re.DOTALL)
# Αpalifi tags me olo tous to periexomeno
rexp2 = re.compile(r'<(script|style).*?>.*?</\1>', re.DOTALL)
# Ejagogi & ektiposi tou sindesmou apo tags
rexp3 = re.compile('<a.*?href="(.+?)".*?>(.*?)</a>', re.DOTALL)
# Apalifi olon ton tags apo to keimeno
rexp4 = re.compile('<.+?>', re.DOTALL)
# Metatropi ton eidiko HTML entities pou uparxoun sto keimneo
rexp5 = re.compile('&amp;|&gt;|&lt;|&nbsp;')
# Metatropi akolou8ion sinexomenon xaraktiron whitespace se ena akribos keno
rexp6 = re.compile(r'\s+')

# anoigma kai diabasma tou arxeiou & apo8ikeusi tou neou se ena arxeio
with open('testpage.txt', 'r', encoding="utf8") as fp:

    text = fp.read()

    for m in rexp.finditer(text):
        print(m.group(1), '\n')

    # Metatropi me xrisi me8odou sub me «callback»
    text = rexp1.sub(' ', text)
    text = rexp2.sub(' ', text)

    for m in rexp3.finditer(text):
        print(m.group(1), m.group(2), '\n')

    text = rexp4.sub(' ', text)
    text = rexp5.sub(function, text)
    text = rexp6.sub(' ', text)
    print(text)
