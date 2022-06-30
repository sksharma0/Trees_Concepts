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
		print(root.val,end=' ')
		pre(root.left)
		pre(root.right)

def solver(node):
	global prev
	if not node:
		return
	solver(node.right)
	solver(node.left)
	node.right=prev
	node.left=None
	prev=node
	return node

#iterative approach
def solver2(node):
	st=[]
	st.append(node)
	while st:
		curr=st.pop()
		if curr.right:
			st.append(curr.right)
		if curr.left:
			st.append(curr.left)
		if st:
			curr.right=st[-1]
		curr.left=None
	return node

def solver3(node):
	curr=node
	while curr:
		if curr.left:
			temp=curr.left
			while temp.right:
				temp=temp.right
			temp.right=curr.right
			curr.right=curr.left
		curr=curr.right
	return node

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

pre(root)
print()

prev=None 
ans=solver2(root)

while ans:
	print(ans.val,end=' ')
	ans=ans.right
