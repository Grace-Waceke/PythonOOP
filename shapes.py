

class circle:
    def __init__(self, r):
        self.radius = r

    def area(self):
        area = 3.14*self.radius**2
        return area

    def perimeter(self):
        perimeter = 2*self.radius*3.14
        return perimeter

newcircle = circle(9)
print(newcircle.area())
print(newcircle.perimeter())  


class Square:
    def __init__(self, a):
        self.length= a

    def area(self):
        sq = self.length **2
        return sq

    def perimeter(self):
        perimeter = self.length * 4
        return perimeter

newrsquare = Square(4)
print(newrsquare.area())
print(newrsquare.perimeter()) 
 
   

class Rectangle:
   def __init__(self, l, w):
        self.length= l
        self.width= w

   def area(self):
        areas = self.length * self.width
        return areas

   def perimeter(self):
        perimeter = 2*self.length + self.width
        return perimeter

newrectangle = Rectangle(3, 5)
print(newrectangle.area())
print(newrectangle.perimeter()) 
 

class Sphere:
    def __init__(self, r):
         self.radius = r
    def area(self):
        area =4*3.14*self.radius**2
        return area

    def volume(self):
        perimeter = 4/3*self.radius**3
        return perimeter

newsphere = Sphere(9)
print(newsphere.area())
print(newsphere.perimeter())  



        

                


    

        