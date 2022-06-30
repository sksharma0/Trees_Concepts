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

def timeToBurnTree(root, start):
    def bfs(root):
        q=deque()
        q.append(root)
        while q:
            curr=q.popleft()
            if curr.data==start:
                t=curr
            if curr.left:
                par[curr.left]=curr
                q.append(curr.left)
            if curr.right:
                par[curr.right]=curr
                q.append(curr.right)
        return t
    par={}
    t=bfs(root)
    di={}
    d=0
    q=deque()
    q.append(t)
    v={t:1}
    while q:
        n=len(q)
        #print([i.data for i in q])
        for i in range(n):
            curr=q.popleft()
            if curr.left and curr.left not in v:
                q.append(curr.left)
                v[curr.left]=1
            if curr.right and curr.right not in v:
                q.append(curr.right)
                v[curr.right]=1
            if curr in par and par[curr] not in v:
                q.append(par[curr])
                v[par[curr]]=1
        d+=1
    return d-1
