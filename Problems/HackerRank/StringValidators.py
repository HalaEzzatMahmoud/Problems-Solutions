if __name__ == '__main__':
    s = input()
    print(any([str.isalnum(x) for x in s]))
    print(any([str.isalpha(x) for x in s]))
    print(any([str.isdigit(x) for x in s]))
    print(any([str.islower(x) for x in s]))
    print(any([str.isupper(x) for x in s]))