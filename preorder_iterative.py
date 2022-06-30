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
def preorder(root):
	st=[root]
	ans=[]
	while st:
		curr=st.pop()
		ans.append(curr.val)
		if curr.right:
			st.append(curr.right)
		if curr.left:
			st.append(curr.left)
	return ans
def preorder2(root):
	if root:
		ans.append(root.val)
		preorder2(root.left)
		preorder2(root.right)

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
    #     1
    #   2    3
    #  4 5  6 7
    # 1 2 4 5 3 6 7
print(preorder(root))
ans=[]
preorder2(root)
print(ans)

