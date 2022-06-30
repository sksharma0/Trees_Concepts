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


def distanceK(root,target,k):
    def dfs2(var,d):
        di[var]=d
        v[var]=1
        for i in adj[var]:
            if v[i]==0:
                dfs2(i,d+1)
    def dfs(root,par):
        if root:
            v[root.val]=0
            adj[root.val]=[par.val]
            adj[par.val].append(root.val)
            dfs(root.left,root)
            dfs(root.right,root)
    
    adj={-1:[]}
    v={-1:0}
    dfs(root,TreeNode(-1))
    di={}
    #print(adj)
    dfs2(target.val,0)
    ans=[]
    for i in di:
        if di[i]==k and i!=-1:
            ans.append(i)
    return ans

# approach 2nd
def distanceK2(root,target,k):
	def parentmaker(root):
		q=deque()
		q.append(root):
		while q:
			curr=q.popleft()
			if curr.left:
				par[curr.left]=curr
				q.append(curr.left)
			if curr.right:
				par[curr.right]=curr
				q.append(curr.right)

	par={}
	v={}
	parentmaker(root)
	q=deque()
	q.append(target)
	d=0
	while q:
		if d==k:
			break
		n=len(q)
		for i in range(n):
			curr=q.popleft()
			if curr.left and curr.left not in v:
				q.append(curr.left)
				v[curr.left]=1
			if curr.right and curr.right not in v:
				q.append(curr.right)
				v[curr.left]=1
			if curr in par and par[curr] not in v:
				q.append(par[curr])
				v[par[curr]]=1
		d+=1
	return [i.val for i in deque]

