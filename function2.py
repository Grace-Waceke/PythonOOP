# def my_country(country="Uganda"):
#      return f"Hello you are from {country}"
#      return f"Hello {student}you are from {country}"


# def greet_multiple(*names):
#          for name in names:
#              print(f"Hello {name}")

#Write a function thats accepts any number of integers and returns the sum of all of them eg;
#sum(1,2)=3
#sum(1,2,3)=6
#sum(7,8,9,10)=34
from unicodedata import name

# def greet(name, age):
def greet_multiple(**kwargs):
    print(kwargs)
    print(kwargs.keys())
    print(kwargs.values())

greet_multiple(name="Grace")
greet_multiple(name="Grace",age=20)


def greet_multiple(**kwargs):
    keys=kwargs.keys()
    if "country" in keys:
        print (f"hello {kwargs['name']}you are from {kwargs ['country']}")

    elif "age" in keys:
            year= 2022 - kwargs["age"]
            print(f"hello{kwargs['name' ]}you were born in {kwargs['year']}")
    elif "country" in keys:
        print(f"hello from{kwargs['country']}, the answer is {sum}")
    elif not kwargs:
        print("hello a programmer the answer is {sum}")


def sum_and_greet(*args , **kwargs):
    sum=0
    for nums in args:
        sum+=nums
    keys=kwargs.keys()
    if "name" in keys:
        print(f"hello{kwargs['name']}, the answer is {sum}")

sum_and_greet(1,2,3,name="susan")
sum_and_greet(10,20,30,name="Kenya")
sum_and_greet(name="Grace")
sum_and_greet(20,30,name="Rwanda")



    





