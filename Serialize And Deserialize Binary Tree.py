https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/
Depth-First Search (DFS)> pre order> root fist, Left> right> kono kichu na thakle 'N'///sob string a 

class Codec:
    def serialize(self, root):
        res = []
        def dfs(node):
            if not node:
                res.append("N")
                return
            res.append(str(node.val))  ##  N an hole add that node /// node.val> node.left> node.right all recursively
            dfs(node.left)
            dfs(node.right)
        dfs(root)                       # recusively call korbo
        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0                   # split kore index set = 0

        def dfs():
            if vals[self.i] == "N":  # N hole Null node
                self.i += 1
                return None
            node = TreeNode(int(vals[self.i]))  # null na hole node create
            self.i += 1
            node.left = dfs()                   # left a jabe, f
            node.right = dfs()                  # right a jabe res theke 
            return node                         # head 

        return dfs()
