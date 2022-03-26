nb_test = int(input())
t_min = int(input())
t_max = int(input())
 
for i in range(nb_test):
    t_test = int(input())
    if t_min <= t_test <= t_max:
        print("Rien à signaler")
    else:
        print("Alerte !!")
        break 