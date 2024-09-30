def bubblesort(my_list):
    for i in range(len(my_list)-1,0,-1):
        for j in range(i):
            if my_list[j]>my_list[j+1]:
                # t = temp variable, benötigt fürs swappen, temporärer Wertspeicher
                t = my_list[j]
                my_list[j] = my_list[j+1]
                my_list[j+1] = t

import random
my_list = []
for i in range(500):
    my_list.append(random.randrange(0,1000,5))
    

bubblesort(my_list)
print(my_list)
