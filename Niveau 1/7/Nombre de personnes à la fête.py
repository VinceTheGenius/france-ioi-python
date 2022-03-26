nbPersonnes = int(input())
nbMax = 0
nbActuel = 0
for loop in range(nbPersonnes * 2):
   numero = int(input())
   if numero > 0:
      nbActuel = nbActuel + 1
      if nbActuel > nbMax:
         nbMax = nbActuel
   else:
      nbActuel = nbActuel - 1
print(nbMax)