def is_matrix(parameter):
    if not(isinstance(parameter,list)) :
        return  False
    if len(parameter) == 0:
        return False

    isMatrix = True
    for i in range(len(parameter)):
        if not(isinstance(parameter[i],list)) or len(parameter[i]) == 0:
            isMatrix = False
            break
        if i == 0 :
            lineLen = len(parameter[i])
        if len(parameter[i]) != lineLen :
            isMatrix = False
            break
        for j in range(len(parameter[i])):
            if not(type(parameter[i][j]) in (int, float)):
                isMatrix = False

    return isMatrix


def print_matrix(parameter):
    if is_matrix(parameter) == False :
        return "not a matrix"
    
    asciiTable = "\n Matrix : \n\n"
    maxSize = 0
    
    for i in range(len(parameter)):
        for j in range(len(parameter[i])):
            if len(str(parameter[i][j])) > maxSize :
                maxSize = len(str(parameter[i][j]))
    
    
    for i in range(len(parameter)):
        for j in range(len(parameter[i])):
            asciiTable += " | " + str(parameter[i][j])
            asciiTable += (maxSize + 5 - len(str(parameter[i][j])))* " "  
        asciiTable += "\n" + ((maxSize+5)*(len(parameter[0])-1)+1) * "-" +"\n"
    return asciiTable

def row_count(matrix):
    if is_matrix(matrix) == False :
        return None

    return len(matrix)

def column_count(matrix):
    if is_matrix(matrix) == False :
        return None

    return len(matrix[0])

def size(matrix):
    if is_matrix(matrix) == False :
        return None

    return row_count(matrix)*column_count(matrix)

def are_equal(matrix1,matrix2):
    if is_matrix(matrix1)  == False or is_matrix(matrix2) == False :
        return None
    if not( row_count(matrix1) == row_count(matrix2) and column_count(matrix1) == column_count(matrix2)):
        return False

    for i in range(len(matrix2)):
        for j in range(len(matrix1[i])):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True

def is_square(matrix):
    if is_matrix(matrix) == False :
        return None

    return row_count(matrix) == column_count(matrix)

def is_identity(matrix):
    if is_matrix(matrix) == False or not(is_square(matrix)):
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i == j :
                if matrix[i][j] != 1:
                    return False
            elif matrix[i][j] != 0:
                return False

    return True

def is_diagonal(matrix):
    if is_matrix(matrix) == False :
        return None

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i != j and matrix[i][j] != 0:
                return False
    return True

def is_symetric(matrix): 
    if is_matrix(matrix) == False or not(is_square(matrix)):
        return None
    for i in range(row_count(matrix)):
        for j in range(column_count(matrix)):
            if i != j : 
                if matrix[i][j] != matrix[j][i]:
                    return False
    return True

def is_triangular(matrix):
    if is_matrix(matrix) == False :
        return None
    if is_diagonal(matrix) == True:
        return True
    topTriangleIsZero = True
    bottomTriangleIsZero = True
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if i > j  and matrix[i][j] != 0:
                topTriangleIsZero = False                
            if i < j  and matrix[i][j] != 0:
                bottomTriangleIsZero = False       
    return bottomTriangleIsZero or topTriangleIsZero

def identity(n):
    if type(n) != int or n <= 0:
        return None
    m = []
    for i in range(n):
        m.append([])
        for j in range(n):
            if i != j :
                m[i].append(0)
            else :
                m[i].append(1)
    return m

def transpose(matrix):
    if is_matrix(matrix) == False :
        return None
    
    mTransposed = []
    rows = row_count(matrix)
    columns = column_count(matrix)

    for i in range(columns):
        mTransposed.append([])
        for j in range(rows):
            mTransposed[i].append(matrix[j][i])

    return mTransposed

def scalar_add(scalar,matrix):  
    if is_matrix(matrix) == False or (type(scalar) != int and type(scalar) != float) :
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] += scalar
    return matrix


def scalar_multiply(scalar,matrix):  
    if is_matrix(matrix) == False or (type(scalar) != int and type(scalar) != float) :
        return None
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            matrix[i][j] *= scalar
    return matrix
 
def add(matrix1,matrix2):
    if is_matrix(matrix1)==False or is_matrix(matrix2)==False:
        return None
    if row_count(matrix1) != row_count(matrix2) or column_count(matrix1) != column_count(matrix2):
        return None
    
    mAdded = []
    for i in range(len(matrix1)):
        mAdded.append([])
        for j in range(len(matrix1[i])):
            mAdded[i].append(matrix1[i][j]+matrix2[i][j])
    return mAdded

def multiply(matrix1,matrix2):
    if is_matrix(matrix1)==False or is_matrix(matrix2)==False:
        return None
    if column_count(matrix1) != row_count(matrix2) :
        return None
    mMultiplied = []
    for i in range(row_count(matrix1)):
        mMultiplied.append([])
        for j in range(column_count(matrix2)):
            ithRowOfA = matrix1[i]
            jthColumnOfB =[]
            for k in range(row_count(matrix2)):
                jthColumnOfB.append(matrix2[k][j])

            dotProduct = 0
            for k in range(len(ithRowOfA)):
                dotProduct += ithRowOfA[k] * jthColumnOfB[k]
            mMultiplied[i].append(dotProduct)
    return mMultiplied
    # do dot product of row and column

def determinant(m):
    if is_matrix(m)==False:
        return None

    if not(is_square(m)):
        return None
    if  size(m) <= 4:
        return (m[0][0] * m[1][1]) - (m[0][1] * m[1][0])
    else :
        det = 0
        isPlus = True
        for i in range(column_count(m)):
            mult = m[0][i]
            if isPlus == True:
                mult *= 1
            else :
                mult *= -1
            
            smallerMatrix =[]
            for j in range(len(m)):
                smallerMatrix.append(m[j][:])

            smallerMatrix.pop(0)
            for j in range(row_count(smallerMatrix)):
                del smallerMatrix[j][i]
            if isPlus == True:
                isPlus = False
            else :
                isPlus = True

            det +=  mult * determinant(smallerMatrix)
    return det

def is_invertible(matrix):
    if is_matrix(matrix)==False:
        return None

    if not(is_square(matrix)):
        return False
    
    det = determinant(matrix)
    if det == 0:
        return False
    return True

def invertible(matrix):
    if is_matrix(matrix) == False or is_invertible(matrix) == False :
        return None

    if size(matrix) == 4 :
        newMat = [[matrix[1][1],-matrix[0][1]],[-matrix[1][0],matrix[0][0]]]
        scalar = 1 / ((matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0]))
        newMat = scalar_multiply(scalar,newMat)

        return newMat

    det = determinant(matrix)
    detMat = []
    isPlusLine = True
    isPlus = True
    for i in range(row_count(matrix)):
        detMat.append([])
        if isPlusLine == True:
            isPlus = True
        else :
            isPlus = False
        for j in range(column_count(matrix)):
            subMat = []
            for k in range(row_count(matrix)):
                subMat.append(matrix[k][:])
            subMat.pop(i)
            for k in range(row_count(subMat)):
                subMat[k].pop(j)
            subDet = determinant(subMat)
            if isPlus == True :
                subDet *= 1
                isPlus = False
            else :
                subDet *= -1
                isPlus = True
            detMat[i].append(subDet)

        if isPlusLine == False:
            isPlusLine = True
        else :
            isPlusLine = False
    detMat = transpose(detMat) 
    scalar = 1/det
    invertedMat = scalar_multiply(scalar,detMat)
    # calculer determinant
    #gen matrice det
    # assign correct signe
    # transposer la matrice
    # scalar 1/(det matrix) * matrice transposé
    return invertedMat
mDet = [
        [4,-1,1],[4,5,3],[-2,0,0]]
m = [[2,1,-1],[-3,-1,2],[-2,1,2]]
m1 = [[9,8,7],[6,5,4]]
m22 = [[9,8,7,6],[6,5,4,9],[1,2,2,2],[3,4,5,6]]
m33 = [[2,1],[3,4]]
m2 = [[0,0,0],[0,0,0],[0,0,0]]
m3 = [[1,0,1],[1,1,0],[0,0,1]]
mAA = [[0,0],[0,0]]
print(is_triangular([[1,1],[1,1]]))
'''print(print_matrix(m))
print(print_matrix(transpose(m)))
print(is_matrix(11))
print(is_matrix([[1,2,3],[4,3,2]]))
print(print_matrix([[1,2.111 ,3],[4,3,2]]))
print(print_matrix(m))
print(row_count(m))
print(column_count(m))
print(size(m))
print(are_equal(m,m1))
print(is_identity(m2))
print(is_diagonal(m2))
print(print_matrix(identity(2)))
print(print_matrix(scalar_multiply(2,m)))
print(print_matrix(add(m1,m3)))'''
#print(determinant(mDet))
#print(print_matrix(transpose(m1)))
#print(print_matrix(multiply(m,m1)))
