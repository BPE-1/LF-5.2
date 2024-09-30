total = int(input("Willkommen im Versandkostenrechner 1.0\nBitte Einkaufswert eintragen: "))
country = input("Bitte Land eingeben (Japan oder Oesterreich): ")
if country == "Japan":
    if total <= 50:
        print("Die Versandkosten betragen $50")
    elif total <= 100:
        print("Die Versandkosten betragen $25")
    elif total <= 180:
        print("Die Versandkosten betragen $5")
    else: 
        print("Der Versand ist kostenlos")
elif country == "Oesterreich":
    if total <= 50:
        print("Die Versandkosten betragen $40")
    else: 
        print("Die Versandkosten betragen $15")
else:
    print("Ungültige Ländereingabe")
