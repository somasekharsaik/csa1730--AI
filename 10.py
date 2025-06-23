# Grid: 0 = walkable cell, 1 = obstacle
grid = [
    [0, 0, 0, 0],
    [1, 1, 0, 1],
    [0, 0, 0, 0],
    [0, 1, 1, 0]
]

start = (0, 0)  # Start position
goal = (3, 3)   # Goal position

def a_star_algorithm(start, goal):
    open_set = set([start])
    closed_set = set()

    g = {}
    f = {}

    g[start] = 0
    f[start] = heuristic(start, goal)

    came_from = {}

    while open_set:
        current = None

        for position in open_set:
            if current is None or f[position] < f[current]:
                current = position

        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path

        open_set.remove(current)
        closed_set.add(current)

        for neighbor in get_neighbour(current):
            if neighbor in closed_set:
                continue

            tentative_g = g[current] + 1  # cost is 1 per step

            if neighbor not in open_set:
                open_set.add(neighbor)
            elif tentative_g >= g.get(neighbor, float('inf')):
                continue

            came_from[neighbor] = current
            g[neighbor] = tentative_g
            f[neighbor] = tentative_g + heuristic(neighbor, goal)

    return None  # No path found

def get_neighbour(position):
    x, y = position
    neighbours = []

    # 4-directional movement
    for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
            if grid[nx][ny] == 0:  # only walkable cells
                neighbours.append((nx, ny))
    
    return neighbours

def heuristic(a, b):
    # Manhattan distance
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

# Run the algorithm
path = a_star_algorithm(start, goal)
print("Shortest Path:", path)
