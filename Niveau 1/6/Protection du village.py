nbMaisons=int(input())
absMax = 1
absMin = 1000000
ordMax = 1
ordMin = 1000000
for loop in range(nbMaisons):
   abscisse = int(input())
   ordonnée = int(input())
   if abscisse > absMax:
      absMax = abscisse
   if abscisse < absMin:
      absMin = abscisse
   if ordonnée > ordMax:
      ordMax = ordonnée
   if ordonnée < ordMin:
      ordMin = ordonnée
largeur = absMax - absMin
longueur = ordMax - ordMin
perimetre = (2*largeur)+(2*longueur)
print(perimetre)