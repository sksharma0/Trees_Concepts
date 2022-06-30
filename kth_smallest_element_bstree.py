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

def inorder(root,k):
	global c,ans
	if root:
		inorder(root.left,k)
		if c==k:
			ans= root.val
		c+=1
		inorder(root.right,k)

root=node(5)
root.left=node(3)
root.right=node(7)
root.left.left=node(2)
root.left.right=node(4)
root.right.left=node(6)
root.right.right=node(8)
    
c=1
ans=0
inorder(root,4)
print(ans)


  #     5
  #   3    7
  #  2 4  6 8
  # 2 3 4 5 6 7 8