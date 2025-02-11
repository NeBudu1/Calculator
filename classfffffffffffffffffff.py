from operator import truediv

# a = 4
# b = "fdasfdas"
# c = []
# print(type(c))
#
# class Car:
#     brend = "nike"
#     speed = 5
#     color = "Red"
#
# car1 = Car()
#
# car2 = Car()
# print(car2.speed)
# car1.speed = 1000
# car1.titan = True
#
# print(car1.titan)
class Car2:
    def __init__(self, brend, color, speed, model):
        self.Brend = brend
        self.Color = color
        self.Speed = speed
        self.Model = model
    def texPas(self):
        print(f"Машина: {self.Brend}, Модель: {self.Model}, Скорость: {self.Speed}, Цвет: {self.Color}")
    def asot(self):
        self.Speed += 100
        print(f"Вы ускорились до {self.Speed}")
car3 = Car2("Bober", "Red", 800, "Mk100Lv")
car4 = Car2("Xeno", "Netu", 6, "HY0087IO")
car3.texPas()
car4.texPas()
car3.asot()
car4.asot()


