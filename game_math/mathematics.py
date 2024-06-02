import numpy


def percentage_array(array):
    for i in range(len(array)):
        array[i] = round(array[i], 4)
        array[i] *= 100
    return array


def print_matrix(matrix, size):
    for i in range(size):
        for j in range(size):
            print(round(matrix[i][j], 2), end=' ')
        print()


def saati_matrix(rates):
    for i in range(len(rates)):  # если были получены отрицательные значения (пользовательский ввод) - превращаем их в
        # обратные
        if rates[i] < 0:
            rates[i] = 1 / abs(rates[i])

    matrix = numpy.ones((5, 5))  # составляем единичную матрицу (т.к. по главной диагонали должны остаться единицы)
    current = 0
    index_elem = 0

    for i in range(4, 0, -1):  # заполняем матрицу пользовательскими и обратными пользовательским значениями
        for j in range(5 - i, 5):
            matrix[current][j] = rates[index_elem]
            matrix[j][current] = 1 / rates[index_elem]
            index_elem += 1
        current += 1

    columnn_sums = matrix.sum(axis=0)  # массив сумм столбцов

    for i in range(5):
        for j in range(5):
            matrix[j][i] /= columnn_sums[i]  # нормируем столбцы

    matrix_means = matrix.mean(1)  # находим среднее значение матрицы (1 - для каждой строчки, 0 - для каждого столбца)

    #print(percentage_array(matrix_means))

    return percentage_array(matrix_means)  # возвращаем массив весов критериев в процентах
