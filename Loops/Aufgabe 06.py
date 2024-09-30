x = int(input("Bitte Dezimalzahl eingeben: "))

safelist = []
while x != 0:
        y = x % 2
        safelist.append(y)
        x = x // 2
safelist.reverse()
        
print(safelist)
