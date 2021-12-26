# Write a function that accepts an integer N
# and returns a NxN spiral matrix.

def matrix(n):
    results = []
    for i in range(n):
        results.append([0 for i in range(n)])

    counter = 1
    startRow = 0
    endRow = n-1
    startColumn = 0
    endColumn = n-1

    while startRow <= endRow and startColumn <= endColumn:
        # Top row
        for i in range(startColumn, endColumn+1):
            results[startRow][i] = counter
            counter += 1
        startRow += 1

        # Right column
        for i in range(startRow, endRow+1):
            results[i][endColumn] = counter
            counter += 1
        endColumn -= 1

        # Bottom column
        for i in range(endColumn, startColumn-1, -1):
            results[endRow][i] = counter
            counter += 1
        endRow -= 1

        # Left column
        for i in range(endRow, startRow-1, -1):
            results[i][startColumn] = counter
            counter += 1
        startColumn += 1
    return results


print(matrix(2))
