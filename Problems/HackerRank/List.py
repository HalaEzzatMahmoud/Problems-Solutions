
'''
The Problem's Link :
             https://www.hackerrank.com/challenges/python-lists/problem?isFullScreen=true  

'''

if __name__ == '__main__':
    N = int(input())
    lst = []
    while N != 0:
        inputs = list(input().split())
        command = inputs[0]
        if command == "insert":
            i, e = map(int,inputs[1: ])
            lst.insert(i,e)
        elif command == "print":
            print(lst)
        elif command == "remove":
            e = int(inputs[1])
            lst.remove(e)
        elif command == "append":
            e = int(inputs[1])
            lst.append(e)
        elif command == "sort":
            lst.sort()    
        elif command == "pop":
            lst.pop()
        elif command == "reverse":
            lst.reverse()

        N -= 1

        
