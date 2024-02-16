
'''
The Problem's Link:
               https://codeforces.com/problemset/problem/282/A
'''
n = int(input())
X = 0
while n != 0:
    operation = input()    
    if operation == '++X' or operation == 'X++':
        X += 1
    elif operation == '--X' or operation == 'X--':
        X -= 1
    n -= 1

print(X)