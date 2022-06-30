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

def pre(node):
	if node:
		print(node.val,end=' ')
		pre(node.left)
		pre(node.right)

def solver(root,val):
	if not root:
		return node(val)
	temp=root
	while True:
		if temp.val<val:
			if not temp.right:
				temp.right=node(val)
				break
			temp=temp.right
		else:
			if not temp.left:
				temp.left=node(val)
				break
			temp=temp.left
	return root

def solver2(root,val):
	if not root:
		return node(val)
	if root.val<val:
		root.right=solver2(root.right,val)
	else:
		root.left=solver2(root.left,val)
	return root

root=node(5)
root.left=node(3)
root.right=node(7)
root.left.left=node(2)
root.left.right=node(4)
#root.right.left=node(6)
root.right.right=node(8)

ans=solver(root,6)
pre(ans)
