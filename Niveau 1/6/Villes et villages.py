nbLieux = int(input())
nbVille = 0
for loop in range(nbLieux):
    nbHabitant = int(input())
    if nbHabitant > 10000:
        nbVille += 1
print(nbVille)