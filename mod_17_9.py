import random

# быстрая сортировка
def qsort_random(array, left, right):
    p = random.choice(array[left:right + 1])
    i, j = left, right
    while i <= j:
        while array[i] < p:
            i += 1
        while array[j] > p:
            j -= 1
        if i <= j:
            array[i], array[j] = array[j], array[i]
            i += 1
            j -= 1

    if j > left:
        qsort_random(array, left, j)
    if right > i:
        qsort_random(array, i, right)

# бинарный поиск
def binary_search(array, element, left, right):
    if left > right:            # если левая граница превысила правую,
        return left, right      # значит элемент отсутствует, возвращаем указатели

    middle = (right + left) // 2
    if array[middle] == element:
        return middle           # возвращаем этот индекс
    elif element < array[middle]:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)


# реализация задания
try:
    arrayNum = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
except ValueError as error:
    print("Вы ввели не число!")
else:
    qsort_random(arrayNum, 0, len(arrayNum)-1)
    print('Отсортированный список - ', arrayNum)
    try:
        element = int(input('Введите искомое число - '))
    except ValueError as error:
        print("Вы ввели не число!")
    else:
        try:
            pos_elem = binary_search(arrayNum, element, 0, len(arrayNum))
        except IndexError as error:
            print(f'Введенный элемент больше наибольшего, позиция последнего элемента - {len(arrayNum) - 1}')
        else:
            if type(pos_elem) != int:
                if pos_elem[0] != 0:
                    print(f'Место элемента между позициями {pos_elem[1]} и {pos_elem[0]}.')
                else:
                    print('Введенный элемент меньше наименьшего.')
            else:
                print('Позиция предыдущего элемента в отсортированном списке - ', pos_elem - 1)

#  Последовательность, которую можно подать на вход
#  12 4 2 7 8 9 3 24 28 21 54 87 29 36
