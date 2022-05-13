"""
class - collection of properties( variables + methods)

object - it is a blueprint of a class

"""

class Car:
    price = 100000
    color = 'red'

    def gas_type(self,type_of_gas):
        return type_of_gas

# car_obj = Car()
# print(car_obj)
# print(car_obj.price)
# print(car_obj.color)
# print(car_obj.gas_type('power'))
#
# car_obj2 = Car()
# print(car_obj2)
# print(car_obj2.price)
# print(car_obj2.color)
# print(car_obj2.gas_type('petrol'))



class CarClass:

    def __init__(self, price, color):
        self.car_price = price
        self.car_color = color

# audi = CarClass(200000, 'white')
# bmw = CarClass(300000, 'red')
# print(audi.car_price)
# print(audi.car_color)
# print('#############')
# print(bmw.car_price)
# print(bmw.car_color)


class Person:

    def __init__(self,first_name,last_name):
        self.first_name = first_name
        self.last_name = last_name

    def person_email(self):
        return '{}.{}@gmail.com'.format(self.first_name, self.last_name)

    def person_age(self, age):
        self.age = age
        return 'my age is {}'.format(self.age)

    def test(self):
        return 'test method'

    def demo(self):
        print(self.test())
        return 'demo method'

# mohan_obj = Person('mohan','pemmadi')
# print(mohan_obj.person_email())
# print(mohan_obj.person_age(31))
# # print(mohan_obj.demo())
# print('@@@@@@@@@@@@')
# venky_obj = Person('venky','abc')
# print(venky_obj.person_email())
# print(venky_obj.person_age(32))

""" Class variable vs Instance variable """
class Family:
    sur_name = 'xyz'  # class variable

    def __init__(self,name):
        self.name = name # instance variable

# obj = Family('abc')
# obj2 = Family('123')

# accessing variables through object

# print(obj.name)
# print(obj.sur_name)

# print('################')
# accessing variables though class name

# print(Family.sur_name)
# print(Family.name)

# print('******************')
#
# print(obj2.sur_name)
# print(obj2.name)



""" Inheritance - getting properties from parent class to child class  """

# Single

class SuperClass:
    def sur_name(self):
        return 'xyz'

class SubClass(SuperClass):
    def blood_group(self):
        return 'B +ve'

# child_obj = SubClass()
# print(child_obj.blood_group())
# print(child_obj.sur_name())

# Multi level

class GrandFather:
    net_worth = 10000000
    def sur_name(self):
        return 'xyz'

class Father(GrandFather):
    def blood_group(self):
        return 'B +ve'

class Child(Father):
    def height(self):
        return '165 cm'

# obj = Child()
# print(obj.height())
# print(obj.blood_group())
# print(obj.sur_name())
# print(obj.net_worth)


# Multiple

class Father:
    def blood_group(self):
        return 'B +ve'

class Mother:
    def blood_group(self):
        return 'A +ve'

    def color(self):
        return 'white'

class Son(Father,Mother):
    def occupation(self):
        return 'software engineer'

obj = Son()
print(obj.occupation())
print(obj.color())
print(obj.blood_group())

















