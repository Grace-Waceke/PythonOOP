


# class Student:
#     name="Effence"
#     age=23
#     country="Kenya"
#     school="akirachix"
    

class Students:
        school="akirachix"
        def __init__(self, firstname,lastname, age, country, ):
            self.firstname=firstname
            self.lastname=lastname
            self.age=age
            self.country=country
            

        def greeting(self):
             return f"Hello, I am {self.firstname}{self.lastname}and I am {self.age} years old, born in  from {self.country}, welcome to {self.school}and my short name is "
        def fullname(self):
            return f"{self.firstname}{self.lastname}"  
        def Yob(self,current_year):
            return current_year-self.age
        def initials(self):
            return self.firstname[0].split(), self.lastname[0].split()
        

            


              

    
