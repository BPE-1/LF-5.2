while True:
    try:
        file_size = input("File size with Prefix [KB, MB, GB]: ").upper()
        dl_speed = float(input("Download speed [Mbit/s]: "))
        value = float(file_size[:-2])
        prefix = file_size[-2:]
        # Prefix Check auf KB,MB,GB
        if prefix == "KB" or prefix == "MB" or prefix == "GB":
            break
        else:
            print("Please enter correct Prefix")
    # Check auf falsche Eingabe zb string statt float oder int
    except ValueError:
        print("Wrong Input, please enter a valid number")

# Datengröße umrechnen
if prefix == "KB":
    value = value * 10**3 * 8 / 10**6
elif prefix == "MB":
    value = value * 10**6 * 8 / 10**6
elif prefix == "GB":
    value = value * 10**9 * 8 / 10**6
    
# Variante mit match case 
"""
match prefix:
    case "KB":
        value = value * 10**3 * 8 / 10**6
    case "MB":
        value = value * 10**6 * 8 / 10**6
    case "GB":
        value = value * 10**9 * 8 / 10**6
        """

# Downloadzeit berechnen
seconds = value / dl_speed

# Ausgabe 
if seconds < 60:
    print("Keep watching")
elif seconds < 599:
    print("Short break. Take a coffee")
elif seconds < 1199:
    print("Going to toilet")
elif seconds < 1499:
    print("Watch one Episode of Gurren Lagann")
elif seconds >= 1500:
    print("Switch to another Server") 

# komplexere Zeitanfgabe
days = seconds // 86400
hours = seconds % 86400 // 3600
minutes = seconds % 86400 % 3600 // 60
seconds1 = seconds % 86400 % 3600 % 60

print("Die Downloadzeit würde", seconds, "Sekunden betragen.")
print("Geschätzte Downloadzeit:",days,"Tage",hours,"Stunden",minutes,"Minuten",seconds1,"Sekunden")
