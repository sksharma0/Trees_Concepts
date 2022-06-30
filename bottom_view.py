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

def bottomView(root):
	if not root:
		return []
	d={}
	q=deque()
	q.append([root,0])
	while q:
		curr,v=q.popleft()
		d[v]=curr.val
		 
		if curr.left:
			q.append([curr.left,v-1])
		if curr.right:
			q.append([curr.right,v+1])
	ans=[]
	for i in sorted(d.keys()):
		ans.append(d[i])
	return ans

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print(bottomView(root))