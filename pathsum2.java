import java.util.List;
import java.util.ArrayList;
import java.util.Stack;


 // Definition for a binary tree node.
 class TreeNode {
      int val;
      TreeNode left;
      TreeNode right;
      TreeNode() {}
      TreeNode(int val) { this.val = val; }
      TreeNode(int val, TreeNode left, TreeNode right) {
          this.val = val;
          this.left = left;
          this.right = right;
      }
  }

class Solution {
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        List<List<Integer>> result = new ArrayList<>();
        if (root == null)
        return result;

        Stack<TreeNode> nodeStack =new Stack <>();
        Stack<Integer> sumStack = new Stack<>();
        Stack<List<Integer>> pathStack = new Stack<>();

        nodeStack.push(root);
        sumStack.push(targetSum - root.val);
        pathStack.push(new ArrayList<>(List.of(root.val)));

        while (!nodeStack.isEmpty()) {
            TreeNode currentNode = nodeStack.pop();
            int currentSum = sumStack.pop();
            List<Integer> currentPath = pathStack.pop();

            if (currentNode.left == null && currentNode.right == null && currentSum == 0) {
                result.add(new ArrayList<>(currentPath));
            }

            if (currentNode.left != null) {
                nodeStack.push(currentNode.left);
                sumStack.push(currentSum - currentNode.left.val);

                List<Integer> leftPath = new ArrayList<>(currentPath);
                leftPath.add(currentNode.left.val);
                pathStack.push(leftPath);
            }

              if (currentNode.right != null) {
                nodeStack.push(currentNode.right);
                sumStack.push(currentSum - currentNode.right.val);

                List<Integer> rightPath = new ArrayList<>(currentPath);
                rightPath.add(currentNode.right.val);
                pathStack.push(rightPath);
            }
        }
        
        return result;
    }
}
