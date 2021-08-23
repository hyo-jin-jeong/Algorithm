import sys
sys.stdin = open("/Users/hyojinjeong/Algorithm/dfs/binary_tree.txt", "r")

def DFS(v):
    if v > 7:
        return 
    DFS(v*2)
    DFS(v*2+1)
    print(v, end=" ")

if __name__ == "__main__":
    DFS(1)