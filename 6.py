from collections import deque

def is_goal(state):
    # state = (vacuum_pos, left_status, right_status)
    # statuses: 'Clean' or 'Dirty'
    return state[1] == 'Clean' and state[2] == 'Clean'

def get_successors(state):
    vacuum_pos, left_status, right_status = state
    successors = []

    # Actions: Suck, Move Left, Move Right

    # Suck dirt if dirty in current room
    if vacuum_pos == 'Left' and left_status == 'Dirty':
        successors.append(('Left', 'Clean', right_status))
    elif vacuum_pos == 'Right' and right_status == 'Dirty':
        successors.append(('Right', left_status, 'Clean'))

    # Move vacuum left
    if vacuum_pos == 'Right':
        successors.append(('Left', left_status, right_status))

    
    if vacuum_pos == 'Left':
        successors.append(('Right', left_status, right_status))

    return successors

def bfs(start_state):
    queue = deque()
    queue.append((start_state, [start_state]))
    visited = set()

    while queue:
        state, path = queue.popleft()
        if state in visited:
            continue
        visited.add(state)

        if is_goal(state):
            return path

        for succ in get_successors(state):
            if succ not in visited:
                queue.append((succ, path + [succ]))

    return None

def print_solution(path):
    if not path:
        print("No solution found.")
        return
    for i, state in enumerate(path):
        vacuum_pos, left_status, right_status = state
        print(f"Step {i}: Vacuum at {vacuum_pos}, Left Room: {left_status}, Right Room: {right_status}")

if __name__ == "__main__":
    # Input: vacuum starts at Left, both rooms Dirty
    start_state = ('Left', 'Dirty', 'Dirty')
    solution = bfs(start_state)
    print_solution(solution)
