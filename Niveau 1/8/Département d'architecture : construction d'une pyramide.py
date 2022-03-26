nbPierresMax = int(input())
hauteur = 0
nbPierresNecessaire = 0
while (nbPierresNecessaire + (hauteur+1)*(hauteur+1)) <= nbPierresMax:
   hauteur = hauteur+1
   nbPierresNecessaire += (hauteur*hauteur)
print(hauteur)
print(nbPierresNecessaire) 