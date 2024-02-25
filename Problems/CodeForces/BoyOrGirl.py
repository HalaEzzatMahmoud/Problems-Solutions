'''
The Problem's Link:
                https://codeforces.com/problemset/problem/236/A
'''

str = input()
set1 = set(str)
if len(set1) % 2 == 0:
    print("CHAT WITH HER!")
else:
    print("IGNORE HIM!")
