depense = 0
sommeTotale = 0
dernièreDepense = False
  
while depense != (-1):
   depense = int(input())
   if depense != -1:
      sommeTotale += depense
print(sommeTotale)