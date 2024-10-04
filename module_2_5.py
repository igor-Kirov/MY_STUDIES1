
def get_matrix(n, m, value):
    matrix = []
    if n > 0 and m > 0 and value > 0:
        for i in range(n):
            row_matr = []
            for y in range(m):
                row_matr.append(value)
            matrix.append(row_matr)
    return matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
#result4 = get_matrix(4, 4, 0)
print(result1)
print(result2)
print(result3)
#print(result4)
