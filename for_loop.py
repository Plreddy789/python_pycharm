# repeating the same statement
# traversing means travel from one element to another





# gun=("sam",'apple')
# names=["ram",'syam','pal',32]
# for name in names:
#     print(name)
#     if name=='ram':
#         print("its me")

# numbers=[51,5,3,5,1,6,2]
# for i in numbers:
#     numbers.pop(0)
#     print(len(numbers))
#     print(numbers)


# for else statement
# list=[3,346,564,45745,"rose"]
# for i in list:
#      print(i)
#     # if i==45745:
#     #     break
#     # else:
#     #     print("number is not equal to 45745")
# else:
#     print("successfully executed")
# print("out of else block")

#
# height_string=input("enter your heights in cms seperated by space : ")
# #154 123 145 135 165
# height_list=height_string.split()
#
# count=0
# for i in height_list:
#     count+=1
# print(count)
# for i in range(count):
#     height_list[i]=int(height_list[i])
# s=0
# for i in height_list:
#     s+=i
# print(s)
# avg=s/count
# print(round(avg))
#
# numbers=input("enter the numbers :")
# # 34 4 587 95 21 -58
# numbers_list=numbers.split()
# count=0
# for number in numbers_list:
#     count+=1
# print(f"the length of the list is:{count}")
#
# for i in range(count):
#      numbers_list[i]=int(numbers_list[i])
# maximum_number=numbers_list[0]
#
# for i in numbers_list:
#     if i>maximum_number:
#         maximum_number=i
# print(maximum_number)
















# numbers=[51,5,3,5,1,6,2,25,54,8,87,45]
#
# for i in range(len(numbers)):
#     numbers.pop(0)
#     print(len(numbers))
#     print(numbers)



# numbers = [51, 5, 3, 5, 1, 6, 2]
# i = 0
#
# while i < len(numbers):
#     numbers.pop(0)
#     print(len(numbers))
#     print(numbers)

exp=[1025,5848,2156,4552,5858,4522]
# sum=0000
# for i in exp:
#     sum+=i
# print(sum)
# total=0
# for i in range(len(exp)):
#     print("month:",(i+1),"expenses :",exp[i])
#     total+=exp[i]
# print("total expense :",total)
#

for i in range(6):
    if i%2==0:
        continue
    print(i*i)












