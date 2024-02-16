'''
The Problem's Link:
             https://www.hackerrank.com/challenges/find-a-string/problem?isFullScreen=false
'''
import re
def count_substring(string, sub_string):
    matches = re.finditer('(?='+ sub_string + ')', string)
    counter = 0
    for i in matches:
        counter += 1
    return counter
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    count = count_substring(string, sub_string)
    print(count)

  