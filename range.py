# SYNTATX : range(start,,stop,step)
 # default value for start : 0 & step : 1
# a=range(5)
# print(a[2])
# total=0
# sum=0
# for i in range(1,101):
#     if i%2==0:
#         sum+=i
# print(sum)

for i in range(1,101):
    if i%3==0:
        print("fizz")
    if i%5==0:
        print("buzz")
    if i%3==0 and i%5==0:
        print("fizz buzz")
    if i%3!=0 and i%5!=0:
        print(i)