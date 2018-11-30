def binarysearch(lst, x):
    lower_bound = 0
    upper_bound = len(lst)
    while lower_bound != upper_bound:
        compared_value = (lower_bound + upper_bound) // 2
        if x == lst[compared_value]:
            return compared_value + 1
        elif x < lst[compared_value]:
            upper_bound = compared_value
        else:
            lower_bound = compared_value + 1
    return None


lst = sorted([int(x) for x in input('Введите массив: ').split()])
x = int(input('Введите искомый элемент: '))
print(binarysearch(lst, x))