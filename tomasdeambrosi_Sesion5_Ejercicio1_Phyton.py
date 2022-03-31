import math


def areaTriangulo(base, altura):
    area = (base*altura)/2
    return area

anonimaTriangulo = lambda base, altura: (base*altura)/2

def areaCirculo(radio):
    area = math.pi*(radio**2)
    return round(area, 2)

anonimaCirculo = lambda radio: round(math.pi*(radio**2),2)

area1 = areaTriangulo(10,10)
print(area1)

area2 = anonimaTriangulo(10,10)
print(area2)

area3 = areaCirculo(5)
print(area3)

area4 = anonimaCirculo(5)
print(area4)
