personne = int(input())
 
for loop in range (personne):
   taille = int(input())
   age = int(input())
   poids = int(input())
   cheval = int(input())
   cheveux = int(input())
   criteres = 0
    
   if taille >= 178 and taille <= 182 :
      criteres = criteres + 1
   if age >=34:
      criteres = criteres + 1
   if poids <70:
      criteres = criteres + 1
   if cheval == 0:
      criteres = criteres + 1
   if cheveux == 1:
      criteres = criteres + 1
    
   if criteres == 5 :
      print ("Très probable")
   elif criteres >= 3 :
      print ("Probable")
   elif criteres == 0 :
      print ("Impossible")
   else :
      print ("Peu probable")