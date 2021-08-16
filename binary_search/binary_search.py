import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/binary_search/binary_search.txt", "r")
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort()
lt = 0
rt = n - 1
while lt <=rt:
    mid = (lt + rt)//2
    if a[mid] == m:
        print(mid + 1)
        break
    elif a[mid] < m:
        lt = mid + 1
    elif a[mid] > m :
        rt = mid - 1

