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

def solver(root,l,r):
	if not root:
		return True
	if l<root.val<r:
		return solver(root.left,l,root.val) and solver(root.right,root.val,r)
	return False
