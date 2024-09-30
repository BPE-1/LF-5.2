# zu lang aber okay
a = int(input('Bitte Zahl eingeben: '))
b = int(input('Bitte Zahl eingeben: '))
c = int(input('Bitte Zahl eingeben: '))
values = [a,b,c]
values.sort()
print(values)

# Besser mit input direkt in die Liste
values = [int(input('Bitte Zahl eingeben: ')), int(input('Bitte Zahl eingeben: ')), int(input('Bitte Zahl eingeben: '))]
values.sort()
print(values)


# besser mit for Schleife
values = [int(input('Bitte Zahl eigeben:')) for i in range(3)]
values.sort()
print(values)
