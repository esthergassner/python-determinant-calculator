def determinant(matrix):
    result = 0
    nrRows = len(matrix)
    if nrRows == 1:
        return matrix[0][0]
    elif nrRows == 2:
        a = matrix[0][0]
        b = matrix[0][1]
        c = matrix[1][0]
        d = matrix[1][1]
        return ((a * d) - (b * c))

    else:
        for ix in range(nrRows): #for each item in the top row,
            rowsMinus1 = nrRows - 1
            first = matrix[0][ix]
            #the following is bad. Cannot use * it's a shallow copy! Does bad stuff!
            #reducedMatrix = [[0]*rowsMinus1]*rowsMinus1
            #find out more at https://www.cs.cmu.edu/~112/notes/notes-2d-lists.html
            
            #instead, we have to do the following- a list comprehension! How pythonic.
            reducedMatrix = [ ([0] * rowsMinus1) for row in range(rowsMinus1) ]
            newRow = 0
            newCol = 0
            for row in range(nrRows):
                for col in range(nrRows):
                    if row != 0 and col != ix:
                        reducedMatrix[newRow][newCol] = matrix[row][col]
                        newCol += 1
                        if newCol == (rowsMinus1):
                            newCol = 0
                            newRow += 1
            if ix % 2:
                result -= (first * determinant(reducedMatrix))
            else:
                result += (first * determinant(reducedMatrix))
                       
        return result
matrix = [[1, 7, 3, 2], [2, 13, 5, 6], [5, 9, 3, 1], [2, 10, 9, 32]]
print(determinant(matrix))

            
            
        

