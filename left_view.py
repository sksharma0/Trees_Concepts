import sys
from math import sqrt,gcd
from collections import deque
from collections import OrderedDict
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

def solver(root,l):
	if root:
		if l not in d:
			d[l]=root.val
		solver(root.left,l+1)
		solver(root.right,l+1)
def solver2(root,l):
	if root:
		if l==len(ans):
			ans.append(root.val)
		solver2(root.left,l+1)
		solver2(root.right,l+1)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

d=OrderedDict()
solver(root,0)
print(list(d.values()))

ans=[]
solver2(root,0)
print(ans)