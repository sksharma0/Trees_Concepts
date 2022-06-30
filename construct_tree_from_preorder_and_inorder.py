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

def pre(root):
	if root:
		arr.append(root.val)
		pre(root.left)
		pre(root.right)

def solver(i,l,r):
	if l>r:
		return
	root=node(preorder[i])
	root.left=solver(i+1,l,d[preorder[i]]-1)
	root.right=solver(i+d[preorder[i]]-l+1,d[preorder[i]]+1,r)
	return root

preorder=[1,2,4,5,3,6,7]
inorder=[4,2,5,1,6,3,7]
n=len(preorder)
d={inorder[i]:i for i in range(n)}

ans=solver(0,0,n-1)
arr=[]
pre(ans)
print(arr)