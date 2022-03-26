dateDébut = int(input())
dateFin = int(input())
nbEntrées = int(input())
nbPersonnes = 0
for loop in range (nbEntrées):
   date = int(input())
   if dateDébut <= date and date <= dateFin:
      nbPersonnes = nbPersonnes + 1
print(nbPersonnes)