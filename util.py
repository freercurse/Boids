import math


def excluded(arr: list) -> list:
    for index, x in enumerate(arr):
        temp = list.copy(arr)
        temp.pop(index)
        yield temp


def fishDist(fish1, fish2, dims) -> float:
    x1 = fish1.rect.x + fish1.rect.width/2
    x2 = fish2.rect.x + fish2.rect.height/2
    y1 = fish1.rect.y + fish1.rect.width/2
    y2 = fish2.rect.y + fish2.rect.height/2
    if (fish2.dist/2 < min(x1, x2, y1, y2) and max(x1, x2) < dims['width'] - fish2.dist/2) and (max(y1, y2) < dims['height'] - fish2.dist/2):
        a2 = abs(x1-x2)
        b2 = abs(y1-y2)
        return math.sqrt(a2**2 + b2**2)
    else:
        return 10000
