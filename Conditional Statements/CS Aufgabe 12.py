# Quittiert mit Fehlermeldung und kann str und int entgegen nehmen ohne Absturz
mark = input("Bitte Note (1-6) eingeben: ")
match mark:
    case "1":
        print("sehr gut")       
    case "2":
        print("gut")
    case "3":
        print("befriedigend")
    case "4":
        print("ausreichend")
    case "5":
        print("mangelhaft")
    case "6":
        print("ungenügend") 
    case other:
        print("Fehlerhafte Eingabe !\nBitte nur Noten von 1 bis 6 eingeben")



# Valueerror wird abgefangen, Programm läuft bis zur korrekten Eingabe, Detailierte Fehlermeldung   
while True:
    try:
        mark = int(input("Bitte Note (1-6) eingeben: "))
        if mark in range(7):
            break
        else: 
            print("Die Note muss zwischen 1 und 6 liegen")
    except ValueError:
        print("Fehlerhafte Eingabe !\nBitte nur Noten von 1 bis 6 eingeben")
    
match mark:
    case 1:
        print("sehr gut")       
    case 2:
        print("gut")
    case 3:
        print("befriedigend")
    case 4:
        print("ausreichend")
    case 5:
        print("mangelhaft")
    case 6:
        print("ungenügend") 
        
