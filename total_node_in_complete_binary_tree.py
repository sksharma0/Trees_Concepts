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


def lheight(root):
	ans=0
	while root:
		root=root.left
		ans+=1
	return ans
def rheight(root):
	ans=0
	while root:
		root=root.right
		ans+=1
	return ans
def solver(root):
	if not root:
		return 0
	lh=lheight(root)
	rh=rheight(root)
	if lh==rh:
		return 2**lh-1
	return 1+solver(root.left)+solver(root.right)