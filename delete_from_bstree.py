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

def deleteNode(root,key):
    def solver(node):
        if not node.left:
            return node.right
        if not node.right:
            return node.left
        temp=node.left
        while temp.right:
            temp=temp.right
        temp.right=node.right
        return node.left
    if not root:
        return None
    if root.val==key:
        return solver(root)
    curr=root
    while curr:
        if curr.val<key:
            if curr.right and curr.right.val==key:
                curr.right=solver(curr.right)
            else:
                curr=curr.right
        else:
            if curr.left and curr.left.val==key:
                curr.left=solver(curr.left)
            else:
                curr=curr.left
    return root