testnumber = int(input("Bitte Zahl eingeben: "))
if testnumber <= 1:
    print(testnumber, "ist Keine Primzahl")
else:
    for i in range(2, testnumber):
        if testnumber % i == 0:
            print(testnumber, "ist keine Primzahl")
            break
    else:
        print(testnumber, "ist eine Primzahl")
        
