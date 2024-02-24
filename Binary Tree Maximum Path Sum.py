https://leetcode.com/problems/binary-tree-maximum-path-sum/solutions/603423/python-recursion-stack-thinking-process-diagram/

 class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
		max_path = float("-inf")                   # placeholder to be updated
 		
        def get_max_gain(node):
 		nonlocal max_path                        # This tells that max_path is not a local variable
 		if node is None:
 			return 0
	
 	        gain_on_left = max(get_max_gain(node.left), 0)              # take maximum value between 0 and maximum gain from left branch   -1, -2, -3 > all (-)ve,hence select 0  
 		gain_on_right = max(get_max_gain(node.right), 0)            # 
			
 		current_max_path = node.val + gain_on_left + gain_on_right  # for a simple tree, 1,2,3--> 1+2+3= 6    ///split hole 
 		max_path = max(max_path, current_max_path)                  # select max, -inf, 6 ...> 6 
 			
 		return node.val + max(gain_on_left, gain_on_right)          # split na hole, 1,2,3, return 1+3 = 4 
			
 	get_max_gain(root)                                              # Starts the recursion chain
	return max_path	




