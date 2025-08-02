
def create_list(matrix_str):
    matrix_list = matrix_str.split('\n')
    for i, line in enumerate(matrix_list):
        matrix_list[i] = list(line)
    return matrix_list

def read_matrix(matrix_list):
    column = ''
    column_of_letters = ''
    column_filtered = ''

    for j in range(len(matrix_list[0])):
        for i, line in enumerate(matrix_list):
            column += matrix_list[i][j]
            if matrix_list[i][j].isalpha() is True:
                column_of_letters += matrix_list[i][j]
                column_filtered += matrix_list[i][j]
            else:
                column_filtered += ' '
    column_filtered = ' '.join(column_filtered.split())

    print(f'Neo reads the matrix column by column, from top to bottom, starting from the leftmost column: {column}')
    print(f'Only select alpha characters: {column_of_letters}')
    print(f'Decoded message: {column_filtered}')



matrix_str = '''7ir
Tsi
h%x
i ?
sM#
$a 
#t%'''

matrix_list = create_list(matrix_str)
read_matrix(matrix_list)