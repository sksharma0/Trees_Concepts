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

def dfs(node,p,d):
	if node:
		par[node]=p
		dist[node]=d
		dfs(node.left,node,d+1)
		dfs(node.right,node,d+1)

def lca(a,b):
	if dist[a]>dist[b]:
		a,b=b,a
	d=dist[b]-dist[a]
	while d>0:
		b=par[b]
		d-=1
	while a.val!=b.val:
		a,b=par[a],par[b]
	return a

def lca2(root,a,b):
	if not root or root.val==a.val or root.val==b.val:
		return root
	left=lca2(root.left,a,b)
	right=lca2(root.right,a,b)
	if not left:
		return right
	if not right:
		return left
	return root

root=node(1)
a=root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
b=root.right.right=node(7)

par={}
dist={}
dfs(root,node(-1),0)
print(lca(a,b).val)
print(lca2(root,a,b).val)

