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

def solver(root,val):
	if not root:
		return False
	arr.append(root.val)
	if root.val==val:
		return True
	if solver(root.left,val) or solver(root.right,val):
		return True
	arr.pop()
	return False

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

arr=[]
solver(root,6)
print(arr)
