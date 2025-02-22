class Solution(object):
    def recoverFromPreorder(self, traversal):

        # helper function for tree building
        # curr_depth stores the depth of current subtree root
        # [start, end] stores the start and end indices of current subtree segment
        def treebuilder(curr_depth, start, end): 
            if start > end:
                return None
            
            if start == end:
                return TreeNode(values[start])
            
            root = TreeNode(values[start]) # start index is the root

            # try to find the right subtree root's index
            right_tree_index = -1 
            for i in range(start + 2, end + 1):
                if depths[i] == curr_depth + 1:
                    right_tree_index = i

            if right_tree_index != -1: # right tree exists
                root.left = treebuilder(curr_depth + 1, start + 1, right_tree_index - 1)
                root.right = treebuilder(curr_depth + 1, right_tree_index, end)
            else: # right tree does not exist
                root.left = treebuilder(curr_depth + 1, start + 1, end)

            return root

        # Pre-prossessing: Obtain 2 arrays of values and depths
        values = []
        depths = [0]

        depth = 0
        curr_num = ""
        i = 0

        while i < len(traversal):
            if traversal[i].isnumeric(): # obtain the value
                while i < len(traversal) and traversal[i].isnumeric():
                    curr_num += traversal[i]
                    i += 1
                values.append(int(curr_num))
                curr_num = ""
            else: # obtain the depth of that value by counting dashes
                while i < len(traversal) and not traversal[i].isnumeric():
                    depth += 1
                    i += 1
                depths.append(depth)
                depth = 0

        # build tree and return root
        return treebuilder(0, 0, len(values) - 1)