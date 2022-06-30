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

def postorder(root):
	st1,st2=[root],[]
	while st1:
		curr=st1.pop()
		st2.append(curr.val)
		if curr.left:
			st1.append(curr.left)
		if curr.right:
			st1.append(curr.right)
	return st2[::-1]
def postorder2(root):
	if root:
		postorder2(root.left)
		postorder2(root.right)
		ans.append(root.val)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
root.left.right.left=node(8)
   #     1
   #   2   3
   #  4 5 6 7
   # 4 5 2 6 7 3 1
print(postorder(root))

ans=[]
postorder2(root)
print(ans)
