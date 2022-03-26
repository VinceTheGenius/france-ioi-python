nbPaires = int(input())
for loop in range(nbPaires):
   xMin1 = int(input())
   xMax1 = int(input())
   yMin1 = int(input())
   yMax1 = int(input())
   xMin2 = int(input())
   xMax2 = int(input())
   yMin2 = int(input())
   yMax2 = int(input())
   if xMin1 >= xMax2:
      print("NON")
   elif xMax1 <= xMin2:
      print("NON")
   elif yMax1 <= yMin2:
      print("NON")
   elif yMin1 >= yMax2:
      print("NON")
   else:
      print("OUI")