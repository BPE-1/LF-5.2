speed_driven = float(input("Bitte Ihre gefahrene Geschwindigkeit eingeben: "))
speed_allowed = float(input("Bitte die erlaubte Höchstgeschwindigkeit eingeben: "))

if speed_driven < 100:
    speed_driven *= 0.97
else:
    speed_driven *= 0.95

if speed_driven > speed_allowed:
    speed_violated = speed_driven - speed_allowed
    if speed_violated < 20:
        print("Glück gehabt")
    elif speed_violated < 30:
        print("Bußgeld von 30€")
    elif speed_violated < 50:
        print("Bußgeld von 120€, 1 Punkt und 1 Monat Fahrverbot")
    elif speed_violated > 50:
        print("Bußgeld von 240€, 2 Punkte und 1 Monat Fahrverbot")
    print("Nach Abzug der Toleranz sind Sie", round(speed_driven,2), "km/h gefahren\nDas ist", round(speed_violated,2),"km/h mehr als erlaubt." )
else:
    print("Keine Sorge, Sie waren im Tempolimit")
