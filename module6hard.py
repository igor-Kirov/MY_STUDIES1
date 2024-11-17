import math

class Figure:
    sides_Count = 0
    __color = [0,0,0]
    __sides = []

    def __init__(self):
        filled = False

    def __is_valid_color(self, r, g, b):
        if (r > 0 and r < 255) and (g > 0 and g < 255) and (b > 0 and b < 255):
            filled = True
            return True
        else:
            filled = False
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color= [r,g,b]

    def get_sides(self):
        #g = self.__sides
        #f = list()
        return self.__sides

    def get_color(self):
        #c = []
        #c = self.__color
        return self.__color

    def __len__(self):
        pir = 0
        for i in self.__sides:
            pir += i
        return pir

    def set_sides(self, *new_sides):
        s =new_sides
        if self.sides_Count == len(s):
            self.__sides = list(s)
        elif len(s) == 1:
            for i in range(0, self.sides_Count):
                self.__sides.append(*s[0])
        elif self.sides_Count < len(s) :
            for i in range(0, self.sides_Count):
                self.__sides.append(1)


class Circle(Figure):
    sides_Count = 1
    __radius = 0

    def __init__(self,color, *side):
        if len(color) == 3:
            self.set_color(*color)
        self.set_sides(*side)
        self.__radius = side[0]/(2*math.pi)

    def get_square(self):
        #S=𝞹R2  c2/4𝞹
        s = 0
        s = math.pi*(self.__radius**2)
        return s

class Triangle(Figure):
    sides_Count = 3

    def __init__(self,color, *side):
        if len(color) == 3:
            self.set_color(*color)
        self.set_sides(*side)

    def get_square(self):
        g = self.get_sides()
        if len(g) == 3:
            s = 0
            p = (g[0]+g[1]+g[2])/2
            s = math.sqrt(p*(p-g[0])*(p-g[1])*(p-g[2]))
            return s

class Cube(Figure):
    sides_Count = 12

    def __init__(self, color, *side):
        if len(color) == 3:
            self.set_color(*color)
        self.set_sides(side)

    def get_volume(self):
        g = self.get_sides()
        if len(g) == 12:
            v = g[0] * g[1] * g[2]
            return v


#triangle1 = Triangle((222, 23, 101), 10, 10, 10)
#print('triangle1 ',triangle1.get_color())
#print(triangle1.get_sides())
#print(triangle1.get_square())

circle1 = Circle((200, 200, 100), 10) # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)
 # Проверка на изменение цветов:
circle1.set_color(55, 66, 77) # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15) # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5) # Не изменится
print(cube1.get_sides())
circle1.set_sides(15) # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())