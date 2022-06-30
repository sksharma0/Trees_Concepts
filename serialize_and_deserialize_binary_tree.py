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

def pre(root):
	if root:
		l.append(root.val)
		pre(root.left)
		pre(root.right)

def serializer(root):
	q=deque()
	q.append(root)
	ans=[]
	while q:
		curr=q.popleft()
		ans.append(curr.val if curr!='#' else curr)
		if curr=="#":
			continue
		if curr.left:
			q.append(curr.left)
		else:
			q.append('#')
		if curr.right:
			q.append(curr.right)
		else:
			q.append('#')
	return ans

def deserializer(arr):
	ans=root=node(arr[0])
	q=deque()
	q.append(root)
	i=1
	while q:
		curr=q.popleft()
		if arr[i]!='#':
			curr.left=node(arr[i])
			q.append(curr.left)
		i+=1
		if arr[i]!='#':
			curr.right=node(arr[i])
			q.append(curr.right)
		i+=1
	return ans

root=node(1)
root.left=node(2)
root.right=node(3)
root.right.left=node(4)
root.right.right=node(5)

arr=serializer(root)
ans=deserializer(arr)
l=[]
pre(ans)
print(l)