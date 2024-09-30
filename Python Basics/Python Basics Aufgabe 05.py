"""
Von Gabriel Fahrenheit, dem Erfinder des Thermometers, wurde der Gefrierpunkt von Wasser zu 32 F und der
Siedepunkt zu 212 F festgelegt Schreiben Sie ein Programm, welches einen vom Benutzer eingegebenen
Wert von C in F umrechnet F=c∗95+32
"""

#geht auch 
""" 
c = float(input("Bitte Wert in °C angeben: "))
f = c * (9/5) +32
print(c, "°C sind",round(f,2),"°F")
"""

# schöner ausgeführt
c = float(input("Bitte Wert in °C angeben: "))
f = c * (9/5) +32
print(c, "°C sind",round(f,2),"°F")
if f <= 32:
    print("Der Gefrierpunkt von Wasser wurde erreicht!")
elif f >= 212:
    print("Der Siedepunkt von Wasser wurde erreicht!")
