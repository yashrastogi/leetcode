class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        if not root:
            return ret
        
        q = deque([(root, 0)])  # Use deque for efficient popping from left
        prevDepth = -1  # Initialize prevDepth to -1 to handle the first node
        
        while q:
            curr, depth = q.popleft()
            
            if depth != prevDepth:
                # If the depth changes, add the value of the previous element
                ret.append(curr.val)
                prevDepth = depth
            
            # Add the right child first to process right side view
            if curr.right:
                q.append((curr.right, depth + 1))
            if curr.left:
                q.append((curr.left, depth + 1))
        
        return ret
