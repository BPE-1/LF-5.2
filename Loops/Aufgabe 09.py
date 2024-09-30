#Sieht mega simpel aus, aber hab mich sehr schwer getan mit :/
x = int(input("Bitte Zahl eingeben: "))
primlist = []

for everynumber in range(2, x +1):
    for anzahl in range(2, everynumber):
        if everynumber % anzahl == 0:
            break
    else:
        primlist.append(everynumber)

            
print("Hier ist Ihre Primzahlenliste:\n"+str(primlist))



