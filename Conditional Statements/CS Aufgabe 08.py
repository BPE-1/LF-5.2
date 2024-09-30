ip = input("Bitte IP-Adresse eingeben: ")
ip_list = ip.split(".")


if int(ip_list[0]) < 128:
    print("Netzklasse A\nNetzmaske 255.0.0.0 ")
elif int(ip_list[0]) < 192:
    print("Netzklasse B\nNetzmaske 255.255.0.0 ")
elif int(ip_list[0]) < 224:
    print("Netzklasse C\nNetzmaske 255.255.255.0 ")
elif int(ip_list[0]) < 239:
    print("Netzklasse D\nKeine Netzmaske vorhanden\n Multicast")
elif int(ip_list[0]) <= 255:
    print("Netzklasse E\nKeine Netzmaske vorhanden")
else:
    print("Ungültige Eingabe\nÜberprüfen Sie das IP-Format")
    
