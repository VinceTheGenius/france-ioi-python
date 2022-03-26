nbAretrouver = int(input())
nbproposer = 0
nbEssai = 0
 
while nbproposer != nbAretrouver:
   nbproposer = int(input())
   
   if nbproposer < nbAretrouver:
       print("c'est plus")
   if nbproposer > nbAretrouver:
       print("c'est moins")
   if nbproposer == nbAretrouver:
       print("Nombre d'essais nécessaires :")
   nbEssai = nbEssai + 1
    
print(nbEssai)