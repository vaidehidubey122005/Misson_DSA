from collections import deque

def goodlandElectricity(grid):
    n, m = len(grid), len(grid[0])
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    # Initialize queue for BFS
    queue = deque()
    visited = [[False] * m for _ in range(n)]
    
    # Add all power stations to the queue
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                queue.append((i, j, 0))  # (x, y, distance)
                visited[i][j] = True
    
    total_cost = 0
    
    # BFS to calculate the minimum cost for each cell
    while queue:
        x, y, dist = queue.popleft()
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, dist + 1))
                total_cost += dist + 1  # Add the distance to total cost
    
    return total_cost

# Sample Input
grid = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 0],
    [0, 1, 0, 0]
]

print(goodlandElectricity(grid))  # Output will depend on grid structure
