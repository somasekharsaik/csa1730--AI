from collections import deque

def water_jug_bfs(capacity_a, capacity_b, target):
    # Each state: (amount_in_jug_a, amount_in_jug_b)
    start = (0, 0)
    visited = set()
    queue = deque()
    queue.append((start, []))  # state, path
    
    while queue:
        (a, b), path = queue.popleft()
        
        if (a, b) in visited:
            continue
        visited.add((a, b))
        
        # Check if goal reached
        if a == target or b == target:
            return path + [(a, b)]
        
        # Possible next states
        
        next_states = []
        
        # Fill jug A
        next_states.append(((capacity_a, b), path + [(a, b, 'Fill Jug A')]))
        
        # Fill jug B
        next_states.append(((a, capacity_b), path + [(a, b, 'Fill Jug B')]))
        
        # Empty jug A
        next_states.append(((0, b), path + [(a, b, 'Empty Jug A')]))
        
        # Empty jug B
        next_states.append(((a, 0), path + [(a, b, 'Empty Jug B')]))
        
        # Pour A -> B
        transfer = min(a, capacity_b - b)
        next_states.append(((a - transfer, b + transfer), path + [(a, b, 'Pour A->B')]))
        
        # Pour B -> A
        transfer = min(b, capacity_a - a)
        next_states.append(((a + transfer, b - transfer), path + [(a, b, 'Pour B->A')]))
        
        for state, new_path in next_states:
            if state not in visited:
                queue.append((state, new_path))
    
    return None

def print_solution(solution):
    if not solution:
        print("No solution found.")
        return
    for step in solution:
        if len(step) == 3:
            a, b, action = step
            print(f"Jug A: {a}L, Jug B: {b}L - {action}")
        else:
            a, b = step
            print(f"Jug A: {a}L, Jug B: {b}L (Goal state)")

if __name__ == "__main__":
    capacity_a = 4
    capacity_b = 3
    target = 2

    solution = water_jug_bfs(capacity_a, capacity_b, target)
    print_solution(solution)
