import copy

class Matrix:
    def __init__(self, mat):
        self.mat = mat

    @staticmethod
    def str(A):
        for j in A:
            for i in j:
                print(f"{i:2}", end=" ")
            print()
        return ''
    
    @staticmethod
    def minor(mas,k):
        res=[]
        for r in mas[1:]:
            row=[]
            for j in range(len(r)):
                if j != k:
                    row.append(r[j])
            res.append(row)
        return res
    
    @staticmethod
    def det(mas):
        n=len(mas)
        if n==2:
            return mas[0][0]*mas[1][1]-mas[0][1]*mas[1][0]
        determinant = 0
        sign = 1
        for i in range(n):
            determinant = determinant+sign*mas[0][i]*Matrix.det(Matrix.minor(mas,i))
            sign=-sign
        return determinant  
        
    def __gt__(self, other):
        return (Matrix.det(self.mat) > Matrix.det(other.mat))

    def __lt__(self, other):
        return (Matrix.det(self.mat) < Matrix.det(other.mat))

    def __eq__(self, other):
        return (Matrix.det(self.mat) == Matrix.det(other.mat))
        
    
    def __add__(self, other):
        A = copy.deepcopy(self.mat)
        for i in range(len(A)):
            for i2 in range(len(other.mat[i])):
                A[i][i2] = self.mat[i][i2] + other.mat[i][i2]
        return Matrix.str(A)
        
    
    def __mul__(self, other):
        s = 0
        A = copy.deepcopy(self.mat)
        for i in range(len(A)):
            for i2 in range(len(other.mat[i])):
                for z in range(len(A[i2])):
                    s = s + self.mat[i][z] * other.mat[z][i2]
                A[i][i2] = s
                s = 0
        return Matrix.str(A)

m1 = Matrix([[1,1],
             [2,2]])
m2 = Matrix([[1,2],
             [3,4]])


'''m1 = Matrix([[1,2,3],
             [6,5,4],
             [7,8,9]])
m2 = Matrix([[1,2,5],
             [3,4,20],
             [8,1,2]])'''

'''m1 = Matrix([[2,1,-1],
             [1,2,3],
             [1,2,3]])
m2 = Matrix([[1,3,0],
             [-1,2,1],
             [-2,4,2]])'''

if m1 > m2:
    print('m1 > m2')
if m1 < m2:
    print('m1 < m2')
if m1 == m2:
    print('m1 = m2')
print('Результат сложения двух матриц: ')
print( m1 + m2)
print('Результат произведения двух матриц: ')
print(m1 * m2)
