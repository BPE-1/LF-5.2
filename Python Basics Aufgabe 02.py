# Stromkosten gesamt

stromkosten = 1467.29
grundgebuehr = 132.90

# Berechnung des Durchschnitts
durchschnitt = ((stromkosten + grundgebuehr) / 12)

# Ausgabe
print("Durchschnittliche Stromkosten pro Monat:",round(durchschnitt, 2), "€")
if durchschnitt > 149.50:
    print("Die Stromkosten von monatlich", round(durchschnitt, 2),"€ sind zu hoch")