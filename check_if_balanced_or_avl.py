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

class node:
	def __init__(self,val):
		self.val=val
		self.left=None
		self.right=None
		
def solver(root):
	if not root:
		return 0
	lh=solver(root.left)
	rh=solver(root.right)
	if lh==-1 or rh==-1 or abs(lh-rh)>1:
		return -1
	return 1+max(lh,rh)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print(True if solver(root)>=0 else False)