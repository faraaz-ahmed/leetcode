'''
103. Binary Tree Zigzag Level Order Traversal
Medium
8.6K
227
Companies
Given the root of a binary tree, return the zigzag level order traversal of its nodes' values. (i.e., from left to right, then right to left for the next level and alternate between).

 

Example 1:


Input: root = [3,9,20,null,null,15,7]
Output: [[3],[20,9],[15,7]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: []
 

Constraints:

The number of nodes in the tree is in the range [0, 2000].
-100 <= Node.val <= 100
Accepted
902.4K
Submissions
1.6M
Acceptance Rate
56.3%
'''


class Solution:
    def zigzagLevelOrder(self, root):
        if root == None:
            return None
        queue = [root, 'x']
        low, high, count = 0, 0, 0
        l = []
        i = 0
        while i < len(queue):
            node = queue[i]
            if type(node) == type(" "):
                break
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 1
            if queue[i] == 'x':
                high = i - 1
                if count % 2 == 0:
                    l.append(list(map(lambda x: x.val, queue[low: high + 1])))
                else:
                    temp = queue[low: high + 1]
                    temp.reverse()
                    l.append(list(map(lambda x: x.val, temp)))
                count += 1
                queue.append('x')
                if i + 1 < len(queue):
                    low = i + 1
                i += 1
        return l


'''
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
 func BFS(tree *Tree) []int {
    queue := []*Tree{}
    queue = append(queue, tree)
    result := []int{} 
    return BFSUtil(queue, result)
}
func BFSUtil(queue []*Tree, res []int) []int {
//This appends the value of the root of subtree or tree to the 
//result
    if len(queue) == 0 {
        return res
     }
    res = append(res, queue[0].Value)
    if queue[0].Right != nil {
        queue = append(queue, queue[0].Right)
    }
    if queue[0].Left != nil {
        queue = append(queue, queue[0].Left)
    }
    return BFSUtil(queue[1:], res)
}

func zigzagLevelOrder(root *TreeNode) [][]int {
    var queue [0]int
    queue = append(queue, root)
    var result [0][0]int
    var isEven := false
    queue = append(queue, root)
    result = append(result, queue)
    while (len(queue) > 0){
        if (!isEven) {
            for i := 0; i < len(queue); i++ {
                queue = append(queue, queue[i].left)
                queue = append(queue, queue[i].right)
                // copy(a[i:], a[i+1:]) // Shift a[i+1:] left one index.
                // a[len(a)-1] = ""     // Erase last element (write zero value).
                // a = a[:len(a)-1]     // Truncate slice.
            }
        }
    }
}














'''
