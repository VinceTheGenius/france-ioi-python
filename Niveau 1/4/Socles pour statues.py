etageMax=int(input())
etageMin=int(input())
volume=0

for i in range(etageMin,etageMax+1):
   volume+= i * i

print(volume)