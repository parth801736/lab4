import math

class point:
    
    def __init__(self):
        self.x=0
        self.y=0

def distance_between_points(a,b):
    d1 = a.x - b.x
    d2 = a.y - b.y

    distance = math.sqrt(d1**2 + d2**2)
    return distance

x = point()   
y = point()         
print(x)
print(y)
print(x != y)

p0 = point()
p0.x = 12
p0.y = 10

p1 = point()
p1.x = 45
p1.y = 35
print('Distance is,')
print(distance_between_points(p1, p0))
