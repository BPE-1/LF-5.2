# If Variante
print("Bitte aus folgenden Optionen wählen:\na: Festplatte formatieren\nb: Festplatte waschen\nc: Festplatte trocknen\nd: Programm beenden")
choice = input("Ihre Auswahl: ").lower()
if choice == "a":
    print("Die Festplatte wurde formatiert")
elif choice == "b":
    print("Die Festplatte wurde gewaschen")
elif choice == "c":
    print("Die Festplatte wurde getrocknet")
elif choice == "d":
    print("Das Programm wird beendet")
else: 
    print("Falsche Eingabe")
    
# match case Variante
print("Bitte aus folgenden Optionen wählen:\na: Festplatte formatieren\nb: Festplatte waschen\nc: Festplatte trocknen\nd: Programm beenden")
choice = input("Ihre Auswahl: ").lower()
match choice:
    case "a":
        print("Die Festplatte wurde formatiert")
    case "b":
        print("Die Festplatte wurde gewaschen")
    case "c":
        print("Die Festplatte wurde getrocknet")
    case "d":
        print("Das Programm wird beendet")
    case other:
        print("Falsche Eingabe")
