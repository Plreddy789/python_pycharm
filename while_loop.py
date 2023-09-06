# when we don't know how many times the loop is executed in advance then we use while loop
# while loop is repated until the condition becomes false
# count=2
# while count<6:
#     print(count)
#     count+=1
#     if count==4:
#         break
#     else:
#         print(count)
# else:
#     print("this is else statement")
#
# print('hello,world')

# close=1
# while close<10:
#     print(close)
#     close+=1
#     if close==4:
#         continue
# else:
#     print("else block")
# print("out of else block")
#
# self=0
# while True:
#     print(self)
#     self+=1
#     if self==5:
#         print(self)
#         break
# else:
#     print("good")
#
# print("i am out of race")
#
#
# number=int(input("enter the number : "))
# while number!=-1:
#     print(number)
#     number=int(input("enter a number :"))
#
# else:
#     print("else block")
# print("out of loop")
total=0
value=int(input("enter a value (0 to quit) : "))
while value!=0:
    total+=value
    value=int(input("enter a value : "))
print(total)


