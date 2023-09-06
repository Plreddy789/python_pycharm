e=(1,2,3.5,"reddy")
d=[1,2,3,4,5,64]
print(type(e))
print(e[3])
print(e[:2])
print(e[1:])
print(2 in e)
d[3]=34
print(d)
d[1:3]=["one",5.445]
print(d)
d.insert(2,54)
print(d)
d.remove('one')
print(d)
l={1,2,3,4,5}
for i in l:
    print(i)

q={"name":"ram","age":"25","class":"cse","marks":"234","hobbies":"[eating,reading,excercise]"}
print(q.get("class"))
print(q.items())
print('ram' in q)
q.update({"age":11})
print(q)
print(type(q.get("hobbies")))
q.pop("name")
print(q)
