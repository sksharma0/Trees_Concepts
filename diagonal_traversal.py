import sys
from math import sqrt,gcd
from collections import deque
sys.setrecursionlimit(10**8)
I  =lambda :int(input())
S  =lambda :input().strip()
M  =lambda :map(int,input().strip().split())
L  =lambda :list(map(int,input().strip().split()))
mod=1000000007

##########################################################

def diagonal(root):
    def dfs(root,v):
        if root:
            if v not in d:
                d[v]=[]
            d[v].append(root.data)
            dfs(root.left,v+1)
            dfs(root.right,v)
        
    d={}
    dfs(root,0)
    ans=[]
    for i in d.values():
        ans+=i
    return ans