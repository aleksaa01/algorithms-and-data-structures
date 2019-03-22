def matrix_multiplication(matrix1, matrix2):
    row_len = len(matrix1[0])
    column_len = len(matrix1)
    if column_len != len(matrix2) or row_len != len(matrix2[0]):
        return ValueError('Both matrices have to have same row and column length.')

    new_matrix = [[0] * row_len for _ in range(column_len)]
    for i in range(column_len):
        for j in range(row_len):
            for k in range(row_len):
                new_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return new_matrix


if __name__ == '__main__':
    import sys
    import json

    m1 = json.loads(sys.argv[1])
    print(matrix_multiplication(m1, m1))
