# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        if root==None:
            return 0
        def chk(root):
            if root.left==None and root.right==None:
                return 1
            elif root.left!=None and root.right==None:
                return chk(root.left)+1
            elif root.left==None and root.right!=None:
                return chk(root.right)+1
            else:
                m=min(chk(root.left),chk(root.right))
                return m+1
        return chk(root)