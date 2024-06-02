import numpy


def percentage_array(array):
    for i in range(len(array)):
        array[i] = round(array[i], 4)
        array[i] *= 100
    return array


def print_matrix(matrix, size):  # работает только для квадратных матриц!
    for i in range(size):
        for j in range(size):
            print(round(matrix[i][j], 2), end=' ')
        print()


def matrix_for_criteria(array):  # [30, 25, 15, 40, 20]
    size = len(array)
    CMatrix = numpy.ones(size)
    for i in range(size):  # заполнение матрицы
        for j in range(i + 1, size):
            value1, value2 = array[i], array[j]
            if value1 / value2 > 1:
                coef = round(value1 / value2, 0)
                CMatrix[i][j], CMatrix[i][j] = coef, 1 / coef
            elif value1 / value2 < 1:
                coef = round(value2 / value1, 0)
                CMatrix[i][j], CMatrix[i][j] = 1 / coef, coef
            else:
                CMatrix[i][j], CMatrix[i][j] = 1, 1

    columnn_sums = CMatrix.sum(axis=0)  # массив сумм столбцов

    for i in range(5):
        for j in range(5):
            CMatrix[j][i] /= columnn_sums[i]  # нормируем столбцы

    matrix_means = CMatrix.mean(1)  # находим среднее значение матрицы (1 - для каждой строчки, 0 - для каждого столбца)

    return matrix_means


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

    return matrix_means  # возвращаем массив весов критериев в процентах


def calculate_everything(players_values, rates):
    print(players_values)
    values = players_values.values()
    sids = players_values.keys()

    cofs = numpy.matrix(saati_matrix(rates)).transpose()

    criteria_1 = matrix_for_criteria([x[0] for x in values])
    criteria_2 = matrix_for_criteria([x[1] for x in values])
    criteria_3 = matrix_for_criteria([x[2] for x in values])
    criteria_4 = matrix_for_criteria([x[3] for x in values])
    criteria_5 = matrix_for_criteria([x[4] for x in values])

    criteries = numpy.matrix([criteria_1, criteria_2, criteria_3, criteria_4, criteria_5]).transpose()

    final = criteries.dot(cofs)

    return final
