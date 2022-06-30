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

def changeTree(root): 
    if not root:
        return
    s=0
    if root.left:
        s+=root.left.data
    if root.right:
        s+=root.right.data
    if s<root.data:
        if root.left:
        	root.left.data=root.data
        if root.right:
            root.right.data=root.data
    else:
        root.data=s
        
    changeTree(root.left)
    changeTree(root.right)
    s2=0
    if root.left:
        s2+=root.left.data
    if root.right:
        s2+=root.right.data
    if root.left or root.right:
        root.data=s2