import math


def area(r):
    return math.pi * r ** 2


radii = [1, 2, 0, 0.5, 7.3, 10]

# sposob jeden
# areas = []
# for r in radii:
#     a = area(r)
#     areas.append(a)
#
# print(areas)

# sposob numer dwa
# print(list(map(area, radii)))

# sposb numer trzy
# print(list(map(lambda x: math.pi * x ** 2, radii)))


# mapowanie listy danych, funkcja i baza danych
# temps = [('a', 32), ('b', 43), ('c', 22), ('d', -9)]
# c_to_f = lambda data: (data[0], (9/5)*data[1]+32)
# print(list(map(c_to_f, temps)))


import statistics

data = [1.2, 1.8, 3, 4, -8, 10]
avg = statistics.mean(data)
print(avg)
print(list(filter(lambda x: x > avg, data)))
print(list(filter(lambda x: x < avg, data)))
