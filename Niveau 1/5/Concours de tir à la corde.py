nbMembres = int(input())
totalEquipe1 = 0 
totalEquipe2 = 0
for loop in range(nbMembres):
   totalEquipe1 = totalEquipe1 + int(input())
   totalEquipe2 = totalEquipe2 + int(input())
if totalEquipe1 > totalEquipe2:
   print("L'équipe 1 a un avantage")
if totalEquipe1 < totalEquipe2:
   print("L'équipe 2 a un avantage")
print("Poids total pour l'équipe 1 :", totalEquipe1) 
print("Poids total pour l'équipe 2 :", totalEquipe2)