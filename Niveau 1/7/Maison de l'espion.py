xMin = int(input())
xMax = int(input())
yMin = int(input())
yMax = int(input())
nbMaisons = int(input())
nbAFouiller = 0
for loop in range(nbMaisons):
   x = int(input())
   y = int(input())
   if (xMin <= x) and (x <= xMax) and (yMin <= y) and (y <= yMax):
      nbAFouiller = nbAFouiller + 1
print(nbAFouiller)