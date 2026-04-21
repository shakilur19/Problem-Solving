# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def inOrder(t):
            if t is None:
                return
            inOrder(t.left)
            ans.append(t.val)
            inOrder(t.right)

        inOrder(root)
        return ans
        