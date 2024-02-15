'''
The Problem's Link:
                https://codeforces.com/problemset/problem/158/A
'''


n , k = map(int,input().split())
count = 0
Scores = list(map(int,input().split()))
kth_place_score = Scores[k-1]
for x in Scores:
    if x >= kth_place_score and x > 0:
        count += 1
print(count)
