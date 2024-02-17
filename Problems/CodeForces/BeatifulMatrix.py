'''
The Problem's Link:
                https://codeforces.com/problemset/problem/263/A
'''
matrix = []
for i in range(5):
    newRow = list(map(int,input().split()))
    matrix.append(newRow)
for row in range(5):
    for col in range(5):
        if matrix[row][col] == 1:
            x = row
            y = col 
miniSteps = abs((2 - x)) + abs((2 - y))            
print(miniSteps)
