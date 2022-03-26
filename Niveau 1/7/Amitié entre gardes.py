dateDebutPremier = int(input())
dateFinPremier = int(input())
dateDebutSecond = int(input())
dateFinSecond = int(input())

if (dateFinSecond < dateDebutPremier) or (dateFinPremier < dateDebutSecond):
   print('Pas amis')
else:
    print('Amis')