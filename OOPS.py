# class - blueprint for creating object
# object - implementation of class or instance of class
#
# class Car:
#     manufacture_month=9
#     def __init__(self,name,weight):
#         self.name=name
#         self.weight=weight
#         self.manufacture_year=2023
#     def display(self,max_speed):
#         print(f"hi i am {self.name} and my maximum speed is {max_speed}")
#     def update_man_month(self):
#         self.manufacture_month+=1
# hyundai=Car("verna",2000)
# print(hyundai.manufacture_year,hyundai.weight)
# # print(hyundai.display()) # it gives none output because return statement is not given
# hyundai.display(220)
#
# kia=Car("seltos",2010)
# print(kia.name,kia.manufacture_month)
# kia.update_man_month()
# print(kia.manufacture_month)

# calculating  area and circumferance of circle

class Circle:
    pi=3.14
    def __init__(self,radius=5):
        self.radius=radius
        self.area=Circle.pi*radius*radius
    def get_cirucmferance(self):
        return 2*Circle.pi*self.radius
    def get_area(self):
        return Circle.pi*self.radius*self.radius

circle_1=Circle(6)
print(circle_1.get_cirucmferance())
print(circle_1.get_area())
print(circle_1.area)
circle_2=Circle(40)
print(circle_2.get_cirucmferance())


#find out the rectangle area
class Rectangle:
    def __init__(self,length,width):
        self.length=length
        self.width=width
    def get_area(self):
        return self.length*self.width
rectangle_1=Rectangle(5,3)
print(rectangle_1.get_area())



# INHERITANCE         # Aquring properties from parent class

