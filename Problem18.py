def triangToMatrix(triang):
    mat = []
    dim = len(triang[-1])
    for i in range(1, dim):
        mat.append(triang[i - 1] + [0 for elem in range(dim - i)])

    mat.append(triang[-1])

    return mat

def reduceDimMatrix(mat):
    dim = len(mat)
    new_mat = [row for row in mat[:dim - 2]]
    if dim == 1:
        return mat

    last_row = []
    for i in range(dim - 1):


if __name__ == '__main__':

    triang = [[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]
    print(triangToMatrix(triang))
