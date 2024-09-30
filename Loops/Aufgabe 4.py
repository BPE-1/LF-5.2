a = int(input("Bitte Zahl 1 eingeben: "))
b = int(input("Bitte Zahl 2 eingeben: "))

while b != 0:
    if a == 0:
        print("ggT ist :",b)
        break
    if a > b:
        a = a - b
    else: 
        b = b - a 
print("ggT ist",a)  
    
if a == 0:
    print("ggT ist :",b)
