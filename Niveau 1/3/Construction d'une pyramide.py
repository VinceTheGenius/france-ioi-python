total=1
largeur=17
for i in range(17):
   if i%2==0:
      continue
   total+=largeur**3
   largeur-=2

print(total)