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
	def __init__(self,key):
		self.val=key
		self.left=None
		self.right=None

def pre(root):
	if root:
		pre(root.left)
		arr.append(root.val)
		pre(root.right)

def solver(i,l,r):
	if l>r:
		return
	root=node(postorder[i])
	root.right=solver(i-1,d[postorder[i]]+1,r)
	root.left=solver(i-r+d[postorder[i]]-1,l,d[postorder[i]]-1)
	return root

postorder=[4,5,2,6,7,3,1]
inorder=[4,2,5,1,6,3,7]
n=len(postorder)
d={inorder[i]:i for i in range(n)}
ans=solver(n-1,0,n-1)

arr=[]
pre(ans)
print(arr)
#    1
#  2  3
# 4 5 6 7