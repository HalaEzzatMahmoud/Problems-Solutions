
'''
The Problem's Link:
                https://codeforces.com/problemset/problem/231/A
'''

n = int(input())
count = 0

while n != 0 :
    opinion = list(map(int,input().split()))
    if sum(opinion) >= 2:
        count += 1
    n -= 1

print(count)


