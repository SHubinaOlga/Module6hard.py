import math
from math import pi

class Figure:
    sides_count = 0

    def __init__(self, color=(0,0,0), *sides: int):
        self.sides = sides
        if len(sides) != self.sides_count:
            self.__sides = [1] * self.sides_count
        else:
            self.__sides = [i for i in sides]
        self.__color = [*color]
        self.filled = True

    def get_color(self):
        return [i for i in self.__color]

    def _is_valid_color(self, *color):
        lst = [*color]
        lst.sort()
        if lst[0] <= 0 or lst[-1] >= 255:
            return False
        else:
            return True

    def set_color(self, *color):
        if self._is_valid_color(*color):
          self.__color = [*color]

    def __is_valid_sides(self, sides):
        res = []
        for i in sides:
            if isinstance(i, int) and i > 0:
                res.append(i)
        if len(res) > 0 and len(sides) == len(self.__sides):
            return True
        else:
            return False

    def set_sides(self, *sides):
        if self.__is_valid_sides(sides):
           self.__sides = sides

    def get_sides(self):
        return [*self.__sides]

    def __len__(self):
        return sum(self.__sides)

class Circle(Figure):
    sides_count = 1

    def __init__(self, color: str, *sides: int):
        super().__init__(color, *sides)
        self.sides = sides
        self.color = color
        self._radius = self.get_sides()[0]  / (2 * math.pi)

    def get_radius(self):
        return self._radius

    def get_square(self):
        return math.sqrt((self._radius * (self._radius - self.sides[0]) * (self._radius - self.sides[1]) * (self._radius - self.sides[2])))

class Triangle(Figure):
    sides_count = 3

    def __init__(self, *sides: int):
        super().__init__(*sides)

    def get_square(self):
        p = len(self) / 2
        a, b, c = self.get_sides()
        return math.sqrt(p * (p - a) * (p - b) * (p - c))

    def get_sides(self):
        p = len(self)/ 2
        return math.sqrt(p * (p - self.sides[0]) * (p - self.sides[1]) * (p - self.sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides: int):
        super().__init__(color, *[sides] * self.sides_count)
        if len(sides) == 1:
            self.__sides = self.sides_count * [i for i in sides]
        else:
            self.__sides = [1] * self.sides_count

    def get_sides(self):
       return [*self.__sides]

    def get_volume(self):
        return self.__sides[0] ** 3

circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

    # Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
print(len(circle1))

    # Проверка объёма (куба):
print(cube1.get_volume())
