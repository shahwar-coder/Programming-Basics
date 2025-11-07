'''
Task: Write a function is_identity(matrix) that takes a square matrix (a list of lists) and returns True if it is an identity matrix (1’s on the diagonal, 0’s elsewhere), else False.

# Example input 1:
matrix = [
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
]
print(is_identity(matrix))
# Expected output: True

# Example input 2:
matrix = [
    [1, 0],
    [1, 1]
]
print(is_identity(matrix))
# Expected output: False   # because matrix[1][0] is 1, not 0
'''

def is_identity(matrix):
    n=len(matrix) #returns number of rows
    for i in range(n):
        for j in range(n):
            if i==j and matrix[i][j]==1:
                continue
            elif i!=j and matrix[i][j]==0:
                continue
            else:
                return False
    return True

if __name__=="__main__":
    try:
        matrix_size=int(input("Length of matrix nxn : "))
        matrix=[]
        for line in range(matrix_size):
            row=input()
            row_as_list=list(map(int, row.split()))
            matrix.append(row_as_list)
        print(is_identity(matrix))
    except Exception:
        print("Invalid Input!")
