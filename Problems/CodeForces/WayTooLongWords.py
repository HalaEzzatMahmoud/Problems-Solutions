
'''
The Problem's Link:
                 https://codeforces.com/problemset/problem/71/A
'''

n = int(input())
inputs = []
while n != 0 :
    str = input()
    str.lower()
    inputs.append(str)
    n -= 1
for x in inputs:
    if len(x) > 10:
        print(x[0],len(x[1:-1]),x[-1], sep="")
    else :
        print(x)    

