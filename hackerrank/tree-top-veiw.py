from collections import deque, defaultdict

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def topView(root):
    if not root:
        return []

    # Queue for level order traversal (node, horizontal distance)
    queue = deque([(root, 0)])
    
    # Map to store the first node at each horizontal distance
    horizontal_distance_map = defaultdict(int)

    while queue:
        node, horizontal_distance = queue.popleft()

        # If this is the first time we encounter this horizontal distance, add the node to the map
        if horizontal_distance not in horizontal_distance_map:
            horizontal_distance_map[horizontal_distance] = node.val

        # Move to left and right child
        if node.left:
            queue.append((node.left, horizontal_distance - 1))
        if node.right:
            queue.append((node.right, horizontal_distance + 1))
    
    # Sort the map by horizontal distance and return the corresponding values
    sorted_keys = sorted(horizontal_distance_map.keys())
    result = [horizontal_distance_map[key] for key in sorted_keys]
    return result
