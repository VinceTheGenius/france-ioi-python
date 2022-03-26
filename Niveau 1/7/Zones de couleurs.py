class point:
    def __init__(self, x, y):
       self.x = x
       self.y = y
 
class zone:
   def __init__(self, top, bottom, left, right):
       self.top = top
       self.bottom = bottom
       self.left = left
       self.right = right
        
   def collide(self, point):
      if point.x < self.left or point.x > self.right or point.y > self.bottom or point.y < self.top:
         return False
      return True
 
small_yellow = zone(20, 45, 25, 50)
blue = zone(10, 55, 10, 85)
first_red = zone(60, 70, 15, 45)
other_red = zone(60, 70, 60, 85)
  
nb = int(input())
  
for i in range(nb):
    x = int(input())
    y = int(input())
     
    p = point(x, y)
     
    if small_yellow.collide(p):
       print('Dans une zone jaune')
    elif blue.collide(p):
       print('Dans une zone bleue')
    elif first_red.collide(p) or other_red.collide(p):
       print('Dans une zone rouge')
    elif x < 0 or y < 0 or x > 90 or y > 70:
       print('En dehors de la feuille')
    else:
       print("Dans une zone jaune")