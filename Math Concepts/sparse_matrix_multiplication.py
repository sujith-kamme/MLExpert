def sparse_matrix_multiplication(matrix_a, matrix_b):
    '''
    SAMPLE INPUT:
      "matrix_a": [
        [0, 2, 0],
        [0, -3, 5],
      ],
      "matrix_b": [
        [0, 10, 0],
        [0, 0, 0],
        [0, 0, 4],
      ]

    SAMPLE OUTPUT:
    [
        [0, 0, 0],
        [0, 0, 20],
    ]
    
    RETURNS [[]] if multiplication cannot be performed
    '''

    row_length_matrix_a = len(matrix_a)
    column_length_matrix_a = len(matrix_a[0])

    row_length_matrix_b = len(matrix_b)
    column_length_matrix_b = len(matrix_b[0])

    if column_length_matrix_a != row_length_matrix_b:
        return [[]]
    
    result = [[0 for _ in range(column_length_matrix_b)] for _ in range(row_length_matrix_a) ]
    
    for i in range(row_length_matrix_a):
        for k in range(column_length_matrix_a):
            if matrix_a[i][k] != 0:
                for j in range(column_length_matrix_b):
                    if  matrix_b[k][j] != 0:
                        result[i][j] += matrix_a[i][k] * matrix_b[k][j]
            
    return result