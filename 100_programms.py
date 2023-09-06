# QUESTION 1
# l=[]
# for i in range(2000,3201):    # given range is taken
#     if i%7==0 and i%5!=0:    #  apply the condition
#         l.append(str(i))      # adding  one by one to list l in string formatt
# print(",".join(l))        # , used for comma seperated values and join them with l without []

#  QUESTION 2
# finding factorial
# first way
# import math
# print(math.factorial(8))
#second way
# def fact(x):
#     if x==0:
#         return 1
#     else:
#         return x*fact(x-1)
# x=int(input("enter a value : "))
# print(fact(x))


# QUESTION 3
# With a given integral number n, write a program to generate a
# dictionary that contains (i, i*i) such that is an integral number
# between 1 and n (both included). and then the program should print the
# dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# x=int(input("enter a value :"))
# d=dict()
# for i in range(1,x+1):
#     d[i]=i*i
# print(d)

# QUESTION 4
# # take the input from user and print the same values in list and tuple formatt
# values=(input("enter the values in comma seperated :"))
# x=values.split(",")
# t=tuple(x)
# l=list(x)
# print(l)
# print(t)


# # QUESTION 8
# input_values=(input("enter the strings in comma seperated :"))
# sp=(input_values.split(","))
# sp.sort()
# print(",".join(sp))


#QUESTION 9
lines=input("enter the data in line by line :")
print(lines.capitalize())


