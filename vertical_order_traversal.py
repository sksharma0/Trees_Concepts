import sys
from heapq import heapify,heappush,heappop
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
	q=deque()
	q.append([root,0,0])
	ans={}
	while q:
		curr,v,l=q.popleft()
		if v in ans:
			if l in ans[v]:
				heappush(ans[v][l],curr.val)
			else:
				ans[v][l]=[curr.val]
		else:
			ans[v]={l:[curr.val]}
		if curr.left:
			q.append([curr.left,v-1,l+1])
		if curr.right:
			q.append([curr.right,v+1,l+1])
	fans=[]
	for i in sorted(ans):
		col=[]
		for j in sorted(ans[i]):
			col+=ans[i][j]
		fans.append(col)
	return fans

root=node(1)
root.left=node(2)
root.right=node(3)
root.left.left=node(4)
root.left.right=node(5)
root.right.left=node(6)
root.right.right=node(7)
   #-2 -1 0 1 2        
   #     1         0 
   #   2   3       1
   #  4  5  7      2
   #     6
print(solver(root))


