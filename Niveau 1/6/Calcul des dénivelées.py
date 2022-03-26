monteeDecsente = int(input())
 
totalMontee = 0
totalDescente = 0
 
for loop in range(monteeDecsente):
   altitude = int(input())
    
   if altitude > 0:
      totalMontee = totalMontee + altitude
   else :
      totalDescente = totalDescente + (-altitude)
print(totalMontee)
print(totalDescente)