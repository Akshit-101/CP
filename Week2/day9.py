# ---------------------------------- set matrix zeroe's  -----------------------------------

n,m=map(int,input().split())

matrix = []

for i in range(0,n):
    #Making a list of row elements and adding that list to matrix list to make a 2D matrix
    arr = [int(j) for j in input().split()]
    matrix.append(arr)

#Iterating the this outer loop for rows
for i in range(0,n):
    #Iterating the this outer loop for columns
    for j in range(0,m):
        #If zero is encountered 
        if(matrix[i][j]==0):
            #set that entire column elements to -1
            for k in range (0,n):
                if(matrix[k][j]!=0): 
                    matrix[k][j]=-1
            
            #set that entire row elements to -1
            for k in range(0,m):
                if(matrix[i][k]!=0):
                    matrix[i][k]=-1


#Now change the value to zero where -1 is present
for i in range(0,n):
    for j in range(0,m):
        if(matrix[i][j]==-1):
            matrix[i][j]=0

#Printing the resultant matrix
for i in range(0,n):
    for j in range(0,m):
        print(matrix[i][j],end=" ")
    print()

# ---------------------------------- Transpose Matrix  -----------------------------------

def transpose(matrix):

    # Getting the number of rows and columns in the original matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Initializing a new matrix with dimensions cols x rows for the transpose
    transposed_matrix = [[0] * rows for _ in range(cols)]

    # Iterating through the original matrix to fill in the transposed matrix
    for i in range(rows):
        for j in range(cols):
            # Swap the row and column indices
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix2 = [[1, 2, 3], [4, 5, 6]]

print(transpose(matrix1)) 
print(transpose(matrix2)) 
