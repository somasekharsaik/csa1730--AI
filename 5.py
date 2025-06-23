from collections import deque

def is_valid(state):
    M_left, C_left, boat = state
    M_right = 3 - M_left
    C_right = 3 - C_left

    if M_left < 0 or C_left < 0 or M_right < 0 or C_right < 0:
        return False
    if M_left > 0 and C_left > M_left:
        return False

    if M_right > 0 and C_right > M_right:
        return False

    return True

def get_successors(state):
    M_left, C_left, boat = state
    successors = []

    moves = [(1,0), (2,0), (0,1), (0,2), (1,1)]

    for M_move, C_move in moves:
        if boat == 1: 
            new_state = (M_left - M_move, C_left - C_move, 0)
        else:          
            new_state = (M_left + M_move, C_left + C_move, 1)
        
        if is_valid(new_state):
            successors.append(new_state)

    return successors

def bfs():
    start = (3, 3, 1)  
    goal = (0, 0, 0)   
    queue = deque()
    queue.append((start, [start]))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state == goal:
            return path
        if state in visited:
            continue
        visited.add(state)

        for succ in get_successors(state):
            if succ not in visited:
                queue.append((succ, path + [succ]))
    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return
    print("Step-by-step solution (M_left, C_left, Boat_position):")
    for i, state in enumerate(path):
        M_left, C_left, boat = state
        side = 'Left' if boat == 1 else 'Right'
        print(f"Step {i}: Missionaries Left = {M_left}, Cannibals Left = {C_left}, Boat on {side}")

if __name__ == "__main__":
    solution = bfs()
    print_solution(solution)
