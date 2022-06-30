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

def solver2(root):
	ans=[]
	st=deque()
	st.append(root)
	d=0
	while st:
		n=len(st)
		tans=[0]*n
		for i in range(n):
			curr=st.popleft()
			if d==0:
				tans[i]=curr.val
			else:
				tans[n-1-i]=curr.val
			if curr.left:
				st.append(curr.left)
			if curr.right:
				st.append(curr.right)
		ans.append(tans)
		d^=1
	return ans	

def solver(root):
	ans=[]
	st=[root]
	d=0
	while st:
		if d==0:
			ans.append([i.val for i in st])
		else:
			ans.append([i.val for i in st[::-1]])
		child=[]
		for i in st:
			if i.left:
				child.append(i.left)
			if i.right:
				child.append(i.right)
		st=child
		d^=1
	return ans

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)

print(solver2(root))