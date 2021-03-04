def excluded(arr: list) -> list:
    for index, x in enumerate(arr):
        temp = list.copy(arr)
        temp.pop(index)
        yield temp
