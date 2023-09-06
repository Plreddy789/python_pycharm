# list=[1,2,32,3,232,"list",5.65,1,2,32]
# print(list)
# print(list[5][2])
# print(list[-3])
# list.append(44)
# print(list.__sizeof__())
# print(len(list))
#
# input=input("enter the list with space seperated ")
# list=input.split()
# print(list)  # output will be in  string format
lst=[]
lst.append((24,4))
print(lst)
# for i in range(5):
#     lst.append(4)
#     i+=1
#     print(lst)
lst2=["black","gold"]
lst.append(lst2)
print(lst)

print(lst[1][1])
lst.insert(2,33)
lst.extend(["string",25,"new"])
print(lst)
list4=[1,2,3,4,5,34,434,5,4,3,4,3,43,4]
# reversed_list=list(reversed(list4))
# lst.reverse()
# print(lst)
# print(reversed_list)
# list4.remove("black")
print(list4)
list4=[1,2,3,4,5,34,434,5,4,3,4,3,54,5,4,45,4,5,5,8,45,8,43,4]
for i in range(1,7):
    list4.remove(i)
print(list4)

list4.pop()
print(list4)
