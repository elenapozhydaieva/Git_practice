class Car:
    biology_class = 'Transport'
    def __init__(self, car_brand, color, year, id):
        self.car_brand = car_brand
        self.color = color
        self.year = year
        self.__id = id

    def drive(self):
        return 'It can drive!'

    def turn_on(self):
        return 'It can turn_on its engine!'

    def get_id(self):
        return f'Hello! My identity number is {self.__id}'

    def set_id(self, new_id):
        self.__id = new_id

car1 = Car('Ford', 'white', 2020, 'C35550E')
print(car1.biology_class)
print(car1.get_id())
print(car1.car_brand)
print(car1.set_id('5PPP064'))
print(car1.get_id())
# print(car1.__id)
print(car1.__dict__)
print(car1._Car__id)

