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

def inorder(root):
	ans=[]
	st=[]
	while True:
		if root:
			st.append(root)
			root=root.left
		else:
			if not st:
				break
			curr=st.pop()
			ans.append(curr.val)
			root=curr.right
	return ans

def inorder3(root):
      ans=[]
      st=[]
      while st or root:
      	if root:
      		st.append(root)
      		root=root.left
      	else:
      		curr=st.pop()
      		ans.append(curr.val)
      		root=curr.right

def inorder2(root):
	if root:
		inorder2(root.left)
		ans.append(root.val)
		inorder2(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
      #    1
      #  2    3
      # 4 5  6 7

      # 4 2 5 1 6 3 7
print(inorder(root))
ans=[]
inorder2(root)
print(ans)

