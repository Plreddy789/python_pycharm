"""arguments"""

# def greet(name):      # parameters or formal parmeters
#     print(f"hii,{name}")
#     print("are you good")
# greet("jenny")
# greet("ram")      # arguments or actual parameters

# def add(a,b):
#     c=a+b
#     print(f"sum ={c} ")
# add(5,6)
# add(3,8)


# def greet(name, dept,subject="c+"):   # here subject is default
#     print(f"hiii,{name}")
#     print(f"are you from {dept} department")
#     print(f"do you teach {subject}")


# greet("plreddy", "civil")  # POSITIONAL ARGUMENT
# greet("ece", "plreddy")  # if is not correct but gives output
# greet(dept="eee", name="pawan")  # KEYWORD ARGUMENT
# greet("plreddy", dept="ece")  # combination of positional argumrnt at first and keyword argument
# greet("plreddy","cse")      # DEFAULT ARGUMENT


""" *args """
# def add(*numbers):
#     c=0
#     for i in numbers:
#         c=c+i
#     print(f"sum={c}")
#
# add(2,2,5,4,6,8,45,6,8,4,5,5)    # ARBITARTY POSITIONAL ARGUMERNTS ( *args)
#
# def multiply(*numbers):
#     j=1
#     for i in numbers:
#         j*=i
#     print(j)
#
# multiply(2,4,5,3)

"""   **kwargs
"""
# def info(**kwargs):
#     for key,values in kwargs.items():
#         print(key,values)
#
#
# info(name="plreddy",age=23,gender="male")   # here 3 argumets
# info(name="plreddy",gender="male")  # here 2 argumrnts
#
#
#
#
#
# # we can use both args and kwargs
# def info(*args,**kwargs):
#     for key, values in kwargs.items():
#         print(key, values)
#
#
# info(1,2,2,3,3,24,name="plreddy", age=23, gender="male")
# info(57,75,8754,name="plreddy", gender="male")

# calculating no of cans of paint required for a wall
# import math
# def paint(length,width,coverage=7):
#     paint_requied=math.ceil(length*width/coverage)
#    # no_of_cans=math.ceil(paint_requied)  # ceil is used to round UP the number to next integer
#     print(f"your wall required {paint_requied} paint cans")
# len=int(input("enter your wall length :"))
# w=int(input("enter your wall width :"))
# paint(length=len,width=w)

#


""" FINDING A PRIME NUMBEER
"""
# def prime_checker(number):
#     is_prime = True
#     if number==1:
#         is_prime=False
#     for i in range(2, number):    # range(2,math.ceil(number/2)+1
#         if number % i == 0:
#             is_prime = False
#     if is_prime == True:
#         print("it is a prime number")
#     else:
#         print("it is not a prime number")
#
#
# number = int(input("enter a number :"))
# prime_checker(number)


"""sieve_of_eratosthenes
to find prime numbers in given range
"""


# def sieve_of_eratosthenes(limit):
#     primes = []
#     is_prime=[True]*(limit+1)
#     for num in range(2,limit+1):
#         if is_prime[num]:
#             primes.append(num)
#             for multiple in range(num*num,limit+1,num):   #(4,11,2)
#                 is_prime[multiple]=False
#     return primes
# limit=int(input("enter a number : "))
# prime_numbers=sieve_of_eratosthenes(limit)
# print(f"prime numbers for  given range of {limit} is :{prime_numbers}")
#
