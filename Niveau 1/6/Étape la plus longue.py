nbJours = int(input())
distanceMax = 0
for loop in range (nbJours):
   distanceParcourue = int(input())
   if distanceParcourue > distanceMax:
      distanceMax = distanceParcourue
print(distanceMax)