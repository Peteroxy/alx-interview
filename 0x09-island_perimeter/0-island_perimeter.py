def island_perimeter(grid):
    if not grid or not grid[0]:
        return 0

    rows = len(grid)
    cols = len(grid[0])
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += 4  # Count all sides initially

                # Check neighbors
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 2  # Subtract two sides (top and bottom)
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 2  # Subtract two sides (left and right)

    return perimeter
