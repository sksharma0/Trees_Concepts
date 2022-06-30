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

	# for 1 based indexing
	#        i
	#  (2*i)  (2*i+1)

	# for 0 based indexing
	#        i
	#  (2*i+1)  (2*i+2)


def widthOfBinaryTree(root):
    if not root:
        return 0
    q=deque()
    q.append([root,0])
    ans=1
    while q:
        n=len(q)
        ans=max(ans,q[-1][1]-q[0][1]+1)
        mn=q[0][1]
        for i in range(n):
            curr,v=q.popleft()
            if curr.left:
                q.append([curr.left,2*(v-mn)+1])
            if curr.right:
                q.append([curr.right,2*(v-mn)+2])
    return ans