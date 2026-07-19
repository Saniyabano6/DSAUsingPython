# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        if root==None:
            return False
        def chk(root,target):
            if root==None:
                return False
            if root.val==target and root.left==None and root.right==None:
                return True
            return chk(root.left,target-root.val) or chk(root.right,target-root.val)
        return chk(root,targetSum)

        