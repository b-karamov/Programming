class Point:
    def __init__(self):
        self.__x = 0
        self.__y = 0

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y


class Shape:
    __figure = ''

    def __init__(self, figure):
        self.__figure = figure

    def get_figure(self):
        return self.__figure

    def __str__(self):
        return self.get_str()


class Quadrangle(Shape):
    __figure = 'Четырёхугольник'

    def set_figure(self, figure):
        self.__figure = figure

    def __init__(self):
        super().__init__(self.__figure)
        self.__a = Point()
        self.__b = Point()
        self.__c = Point()
        self.__d = Point()

    def __set_a(self, tup):
        self.__a.set_x(tup[0])
        self.__a.set_y(tup[1])

    def __set_b(self, tup):
        self.__b.set_x(tup[0])
        self.__b.set_y(tup[1])

    def __set_c(self, tup):
        self.__c.set_x(tup[0])
        self.__c.set_y(tup[1])

    def __set_d(self, tup):
        self.__d.set_x(tup[0])
        self.__d.set_y(tup[1])

    def set_vertexes(self, l):
        self.__set_a(l[0])
        self.__set_b(l[1])
        self.__set_c(l[2])
        self.__set_d(l[3])

    def __triangle_area(self, a, b, c):
        '''
        :param a: точка a
        :param b: точка b
        :param c: точка с
        :return: возвращает площадь треугольника, построенного на этих точках
        '''
        self.__vec_1 = (b.get_x() - a.get_x(), b.get_y() - a.get_y())
        self.__vec_2 = (c.get_x() - a.get_x(), c.get_y() - a.get_y())
        return abs(self.__vec_1[0] * self.__vec_2[1] - self.__vec_2[0] * self.__vec_1[1]) / 2

    def get_area(self):
        area = self.__triangle_area(self.__a, self.__b, self.__c) + self.__triangle_area(self.__d, self.__b, self.__c)
        return area

    def __length(self, a, b):
        return ((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2) ** (1 / 2)

    def __point_name(self, name):
        if name == 'a':
            return self.__a
        if name == 'b':
            return self.__b
        if name == 'c':
            return self.__c
        if name == 'd':
            return self.__d

    def __get_sides(self):
        # возвращает стороны четырехугольника (то есть показывает недиагональные стороны)
        # РАБОТАЕТ ТОЛЬКО ДЛЯ ВЫПУКЛЫХ ЧЕТЫРЕХУГОЛЬНИКОВ
        self.__s = [(self.__length(self.__a, self.__b), 'a', 'b'),
                    (self.__length(self.__a, self.__c), 'a', 'c'),
                    (self.__length(self.__a, self.__d), 'a', 'd')]
        self.__s.sort(key=lambda x: x[0])
        # найдем точку, самую удаленную от точки a
        self.__furthest = {'b', 'c', 'd'}.difference({self.__s[0][2], self.__s[1][2]}).pop()
        self.__adjacent = {'b', 'c', 'd'}.difference({self.__furthest})
        self.__sides = [
            (self.__point_name(self.__s[0][1]), self.__point_name(self.__s[0][2])),
            (self.__point_name(self.__s[1][1]), self.__point_name(self.__s[1][2])),
            (self.__point_name(self.__furthest), self.__point_name(self.__adjacent.pop())),
            (self.__point_name(self.__furthest), self.__point_name(self.__adjacent.pop()))
        ]
        return self.__sides

    def get_lengths(self):  # возвращает длины сторон четырехугольника
        self.__side_points = self.__get_sides()
        self.__l_1 = self.__length(*self.__side_points[0])
        self.__l_2 = self.__length(*self.__side_points[1])
        self.__l_3 = self.__length(*self.__side_points[2])
        self.__l_4 = self.__length(*self.__side_points[3])

        self.__l = [self.__l_1, self.__l_2, self.__l_3, self.__l_4]
        return self.__l

    def get_perimeter(self):
        self.__l = self.get_lengths()
        return sum(self.__l)

    def __is_Integer(self, p):
        integer = True
        if not isinstance(p.get_x(), int):
            integer = False
        elif not isinstance(p.get_y(), int):
            integer = False
        return integer

    def draw_points(self):
        draw = True
        for p in [self.__a, self.__b, self.__c, self.__d]:
            if not self.__is_Integer(p):
                print('Построение возможно только для точек с целочисленными координатами')
                draw = False
                break
        if draw:
            self.__coord = [(self.__a.get_x(), self.__a.get_y(), 'a'),
                           (self.__b.get_x(), self.__b.get_y(), 'b'),
                           (self.__c.get_x(), self.__c.get_y(), 'c'),
                           (self.__d.get_x(), self.__d.get_y(), 'd')
                           ]
            self.__x_max = max(self.__coord, key=lambda x: x[0])[0]
            self.__y_max = max(self.__coord, key=lambda x: x[1])[1]
            self.__x_min = min(self.__coord, key=lambda x: x[0])[0]
            self.__y_min = min(self.__coord, key=lambda x: x[1])[1]
            painting = [['*']*(self.__x_max-self.__x_min+1) for i in range(self.__y_max-self.__y_min+1)]
            for dot in self.__coord:
                painting[-1-(dot[1]-self.__y_min)][dot[0]-self.__x_min] = dot[2]
            painting.insert(0, [i+self.__x_min for i in range(len(painting[0]))])
            for i in range(1, len(painting)):
                painting[i].append(self.__y_max-i+1)
            for line in painting:
                print(*line)


    def get_str(self):
        return ''.join(['______________________________\n',
                        'Фигура: ', self.get_figure(), '\n',
                        'Площадь фигуры: ', str(self.get_area()), '\n',
                        'Периметр фигуры: ', str(self.get_perimeter()), '\n',
                        '______________________________\n'])


class NotRightFigure(Exception):
    pass


class Square(Quadrangle):
    __figure = 'Квадрат'

    def __init__(self):
        self.set_figure(self.__figure)
        super().__init__()

    def __is_Square(self):
        self.__l = self.get_lengths()
        if not (self.__l[0] == self.__l[1] and self.__l[1] == self.__l[2] and self.__l[2] == self.__l[3]
                and self.__l[0]**2 == self.get_area()):
            raise NotRightFigure('Это не квадрат! Введи другие координаты')

q = Square()
q.set_vertexes([(-1,5), (0,1), (1, 2), (1, 0)])

q.draw_points()
print(q)
