x = input("Bitte Binärzahl eingeben: ")
# prüfe ob jedes(all) Zeichen in x entweder 0 oder 1 ist
if all(char in "01" for char in x):
    dec = int(x,2)
    print(dec)
else:
    print("Unültige Eingabe!\nNur 0 & 1 erlaubt!")
