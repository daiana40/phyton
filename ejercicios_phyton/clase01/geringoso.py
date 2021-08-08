cadena = 'Geringoso'
capadepenapa = ''
vocales = 'aeiou'

for c in cadena:    
    if c.lower() in vocales:
        capadepenapa += c + 'p' + c.lower()
    else:
        capadepenapa += c

print(capadepenapa)