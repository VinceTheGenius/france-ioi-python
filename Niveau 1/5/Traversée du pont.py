premierDé = int(input())
secondDé = int(input())
somme = premierDé + secondDé
 
if somme >= 10:
   print ("Taxe spéciale !")
   print (36)
else:
   print ("Taxe régulière")
   print (2 * somme)