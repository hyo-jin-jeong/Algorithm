import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/dfs/recursive_function.txt", "r")

def DFS(n):
    if n == 0:
        return
    DFS(n//2)
    print(n%2, end='')

if __name__ == "__main__":
    n = int(input())
    DFS(n)