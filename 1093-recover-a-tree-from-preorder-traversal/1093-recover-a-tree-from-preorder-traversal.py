class Solution(object):
    def recoverFromPreorder(self, traversal):
        def treebuilder(curr_depth, start, end): 
            if start > end:
                return None
            
            if start == end:
                return TreeNode(values[start])
            
            root = TreeNode(values[start])

            right_tree_index = -1 
            for i in range(start + 2, end + 1):
                if depths[i] == curr_depth + 1:
                    right_tree_index = i

            if right_tree_index != -1: 
                root.left = treebuilder(curr_depth + 1, start + 1, right_tree_index - 1)
                root.right = treebuilder(curr_depth + 1, right_tree_index, end)
            else: 
                root.left = treebuilder(curr_depth + 1, start + 1, end)

            return root

        values = []
        depths = [0]

        depth = 0
        curr_num = ""
        i = 0

        while i < len(traversal):
            if traversal[i].isnumeric(): 
                while i < len(traversal) and traversal[i].isnumeric():
                    curr_num += traversal[i]
                    i += 1
                values.append(int(curr_num))
                curr_num = ""
            else: 
                while i < len(traversal) and not traversal[i].isnumeric():
                    depth += 1
                    i += 1
                depths.append(depth)
                depth = 0

        return treebuilder(0, 0, len(values) - 1)