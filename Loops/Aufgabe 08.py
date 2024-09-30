# Aufgabe ist mir wirklich zu komplex als Anfänger... 
# Ich gehe jetzt einfach mal von einer MAC aus, die als string vorliegt 

mac = "00:80:41:ae:fd:7e"
maclist = mac.split(":")
for maclist_element in maclist:
    decimal = int(maclist_element, 16)
    binary = bin(decimal)
    print(binary[2:].zfill(8))
    
