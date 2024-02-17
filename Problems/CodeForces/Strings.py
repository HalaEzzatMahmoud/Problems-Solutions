'''
The Problem's Link:
                https://codeforces.com/problemset/problem/112/A
'''

str1 = input().split()
str2 = input().split()
str1.sort()
str2.sort()
for x in str1:
    for i in str2:
        if x.lower() > i.lower():
            print(1)
        elif x.lower() < i.lower():
            print(-1)
        else: 
            print(0)
