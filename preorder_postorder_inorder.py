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
	def __init__(self,key):
		self.val=key
		self.left=None
		self.right=None

def prepostin(root):
	pre,ino,post=[],[],[]
	st=[[root,1]]
	while st:
		curr,num=st.pop()
		if num==1:
			pre.append(curr.val)
			st.append([curr,num+1])
			if curr.left:
				st.append([curr.left,1])
		elif num==2:
			ino.append(curr.val)
			st.append([curr,num+1])
			if curr.right:
				st.append([curr.right,1])
		else:
			post.append(curr.val)
	return pre,ino,post

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
print(prepostin(root))