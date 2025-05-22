def queenAttack(board):
    # Get the queen's position
    n = len(board)
    q_x = q_y = -1

    for i in range(n):
        for j in range(n):
            if board[i][j] == 'Q':
                q_x, q_y = i, j
                break

    # Directions: [up, down, left, right, up-left, up-right, down-left, down-right]
    directions = [
        (-1, 0),  # Up
        (1, 0),   # Down
        (0, -1),  # Left
        (0, 1),   # Right
        (-1, -1), # Up-left
        (-1, 1),  # Up-right
        (1, -1),  # Down-left
        (1, 1)    # Down-right
    ]

    count = 0

    # Iterate through each direction and check for attackable squares
    for direction in directions:
        dx, dy = direction
        x, y = q_x, q_y

        while 0 <= x + dx < n and 0 <= y + dy < n:
            x += dx
            y += dy
            if board[x][y] == 'X':  # There's an obstacle
                break
            count += 1

    return count
