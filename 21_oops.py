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

mohan_obj = Person('mohan','pemmadi')
print(mohan_obj.person_email())
print(mohan_obj.person_age(31))
# print(mohan_obj.demo())
print('@@@@@@@@@@@@')
venky_obj = Person('venky','abc')
print(venky_obj.person_email())
print(venky_obj.person_age(32))













