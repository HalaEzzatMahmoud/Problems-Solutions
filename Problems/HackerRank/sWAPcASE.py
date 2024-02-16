'''
The Problem's Link:
         https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true
'''

def swap_case(s):
    str = ""
    for i in s:
        if i.islower() == True: 
            str += i.upper()
        elif i.isupper() == True:
            str += i.lower()
        else:
            str += i

    return str

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)