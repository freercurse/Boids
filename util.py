import math


def excluded(arr: list) -> list:
    for index, x in enumerate(arr):
        temp = list.copy(arr)
        temp.pop(index)
        yield temp


def catDist(mouse, cat, dims) -> float:
    x1 = cat.rect.x + cat.rect.width / 2
    x2 = mouse.rect.x + mouse.rect.height / 2
    y1 = cat.rect.y + cat.rect.width / 2
    y2 = mouse.rect.y + mouse.rect.height / 2
    if (mouse.dist / 2 < min(x1, x2, y1, y2) and max(x1, x2) < dims['width'] - mouse.dist / 2) and (max(y1, y2) < dims['height'] - mouse.dist / 2):
        a2 = abs(x1-x2)
        b2 = abs(y1-y2)
        return math.sqrt(a2**2 + b2**2)
    else:
        return 10000
