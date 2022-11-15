# Проверка на то, что вводятся цифры в последовательность
def check_numbers(array_new):
    while not array_new.replace(" ", "").isdigit():
        array_new = input("Последовательность чисел должна состоять только из цифр и "
                          "пробелов, попробуйте снова: ")
    return array_new


# Проверка на то, что число пользователя цифры
def check_user_element(element):
    while not element.isdigit():
        element = input("Значение должно быть числом: ")
    return element


# Сортировка списка
def sort_numbers(array_correct):
    array_list = array_correct.split()
    array_list = list(map(int, array_list))
    array_list = sorted(array_list)
    return array_list


# Проверка, что число больше или меньше значений в последовательности
def check_range(array_list, element):
    array_list.append(element)
    array = sorted(array_list)
    index_user_number = array.index(element)
    if index_user_number == len(array_list)-1:
        print("Введённое число больше, чем значения в списке")
    elif index_user_number == 0:
        print("Введённое число меньше, чем значения в списке")


def binary_search(array, element, left, right):
    if left > right:  # если левая граница превысила правую,
        return False  # значит элемент отсутствует

    middle = (right + left) // 2  # находимо середину
    if array[middle] == element:  # если элемент в середине,
        print(middle)
        return middle  # возвращаем этот индекс
    elif element < array[middle]:  # если элемент меньше элемента в середине
        if element > array[middle - 1]:
            return middle - 1
        else:
            # рекурсивно ищем в левой половине
            return binary_search(array, element, left, middle - 1)
    else:  # иначе в правой
        return binary_search(array, element, middle + 1, right)


array_new = input("Введите последовательность чисел через пробел: ")
array_current = check_numbers(array_new)
element = input("Пожалуйста, введите число, по отношению к которому будет произведён поиск: ")
element_current = int(check_user_element(element))
array_list = sort_numbers(array_current)
index = binary_search(array_list, element_current, 0, len(array_list)-1)
if index:
    print(index)
else:
    check_range(array_list, element_current)
