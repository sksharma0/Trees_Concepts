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

def isleaf(node):
	return (not node.left) and (not node.right)

def solver(root):
	lb,rb,l=[],[],[]
	temp=root
	while temp:
		if temp.left:
			lb.append(temp.val)
			temp=temp.left
		elif temp.right:
			lb.append(temp.val)
			temp=temp.right
		else:
			break
	temp=root.right
	while temp:
		if temp.right:
			rb.append(temp.val)
			temp=temp.right
		elif temp.left:
			rb.append(temp.val)
			temp=temp.left
		else:
			break
	st=[]
	while True:
		if root:
			st.append(root)
			root=root.left
		else:
			if not st:
				break
			curr=st.pop()
			if isleaf(curr):
				l.append(curr.val)
			root=curr.right
	return lb+l+rb[::-1]

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

   #     1
   #   2   3
   #  4 5 6 7
   # 1 2 4 5 6 7 3

print(solver(root))
