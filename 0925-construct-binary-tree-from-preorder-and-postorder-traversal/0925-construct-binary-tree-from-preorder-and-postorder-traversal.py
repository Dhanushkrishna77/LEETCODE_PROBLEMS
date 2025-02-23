
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):

        if not preorder and not postorder:
            return None
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root
        left_val = preorder[1]
        left_index = postorder.index(left_val)
        left_size = left_index + 1
        root.left = self.constructFromPrePost(preorder[1: left_size + 1], postorder[: left_size])
        root.right = self.constructFromPrePost(preorder[left_size+1:], postorder[left_size : -1])
        return root