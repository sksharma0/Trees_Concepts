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
	ans=[]
	while root:
		#print(root.val,ans)
		temp=root.left
		if not temp:
			ans.append(root.val)
			root=root.right
			continue
		while temp.right and temp.right!=root:
			temp=temp.right
		if temp.right==root:
			temp.right=None
			root=root.right
		else:
			temp.right=root
			ans.append(root.val)
			root=root.left
		# if len(ans)==5:
		# 	break
	return ans

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print(solver(root))
