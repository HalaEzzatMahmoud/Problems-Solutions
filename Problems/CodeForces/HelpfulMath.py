'''
The Problem's Link:
                https://codeforces.com/problemset/problem/339/A
'''

str = input().strip()
digits = []
for i in str:
    if i.isdigit():
        digits.append(i)
digits.sort()
str1 = '+'.join(digits)
print(str1)
































