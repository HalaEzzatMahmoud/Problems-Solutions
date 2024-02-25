'''
The Problem's Link:
                https://codeforces.com/problemset/problem/281/A
'''

'''str = input()
lst = []
for i in range(len(str)):
    if i != 0:
        lst.append(str[i])
    else:
        str1 = str[i].capitalize()
        lst.insert(0,str1)
str2 = ''.join(lst)        
print(str2)'''

str = input().strip()
str1 = str[0].upper()
print(str1 + str[1:])