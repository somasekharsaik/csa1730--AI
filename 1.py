from heapq import heappush, heappop

GOAL = (1, 2, 3,
        4, 5, 6,
        7, 8, 0)

MOVES = {
    0: [1, 3],
    1: [0, 2, 4],
    2: [1, 5],
    3: [0, 4, 6],
    4: [1, 3, 5, 7],
    5: [2, 4, 8],
    6: [3, 7],
    7: [4, 6, 8],
    8: [5, 7]
}

def manhattan_distance(state):
    distance = 0
    for idx, tile in enumerate(state):
        if tile == 0:
            continue
        goal_idx = GOAL.index(tile)
        current_row, current_col = divmod(idx, 3)
        goal_row, goal_col = divmod(goal_idx, 3)
        distance += abs(current_row - goal_row) + abs(current_col - goal_col)
    return distance

def get_neighbors(state):
    neighbors = []
    blank_idx = state.index(0)
    for swap_idx in MOVES[blank_idx]:
        new_state = list(state)
        # swap blank with adjacent tile
        new_state[blank_idx], new_state[swap_idx] = new_state[swap_idx], new_state[blank_idx]
        neighbors.append(tuple(new_state))
    return neighbors

def reconstruct_path(came_from, current):
    path = [current]
    while current in came_from:
        current = came_from[current]
        path.append(current)
    return path[::-1]

def a_star(start):
    open_set = []
    heappush(open_set, (manhattan_distance(start), 0, start))
    came_from = {}
    g_score = {start: 0}
    closed_set = set()

    while open_set:
        _, cost, current = heappop(open_set)

        if current == GOAL:
            return reconstruct_path(came_from, current)

        closed_set.add(current)

        for neighbor in get_neighbors(current):
            if neighbor in closed_set:
                continue
            tentative_g_score = g_score[current] + 1

            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + manhattan_distance(neighbor)
                heappush(open_set, (f_score, tentative_g_score, neighbor))

    return None

def print_board(state):
    for i in range(0, 9, 3):
        print(state[i:i+3])
    print()

if __name__ == "__main__":
    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    solution_path = a_star(start_state)

    if solution_path:
        print(f"Solution found in {len(solution_path)-1} moves:")
        for step in solution_path:
            print_board(step)
    else:
        print("No solution found.")
