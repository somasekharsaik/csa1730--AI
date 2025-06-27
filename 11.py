neighbors = {'WA': ['NT', 'SA'], 
'NT': ['WA', 'SA', 'Q'],
'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
'Q': ['NT', 'SA', 'NSW'], 
'NSW': ['SA', 'Q', 'V'], 
'V': ['SA', 'NSW'], 
'T': []
}
colors = ['Red', 'Green', 'Blue']
solution = {}

def solve(states):
    if not states: return True
    state = states[0]
    for color in colors:
        if all(solution.get(n) != color for n in neighbors[state]):
            solution[state] = color
            if solve(states[1:]): return True
            del solution[state]
    return False

if solve(list(neighbors.keys())):
    for s in sorted(solution): print(f"{s}: {solution[s]}")
else:
    print("No solution")
