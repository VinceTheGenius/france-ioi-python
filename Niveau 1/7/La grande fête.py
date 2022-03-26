espionDebut = int(input())
espionFin = int(input())
nbInvites = int(input())
nbSuspects = 0
for loop in range(nbInvites):
   debut = int(input())
   fin = int(input())
   if not( (espionFin < debut) or (fin < espionDebut) ):
      nbSuspects = nbSuspects + 1
print(nbSuspects)