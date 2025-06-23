import itertools

def solve_cryptarithmetic():
    letters = ('S', 'E', 'N', 'D', 'M', 'O', 'R', 'Y')
    digits = range(10)

    for perm in itertools.permutations(digits, len(letters)):
        s, e, n, d, m, o, r, y = perm
        
        # Leading letters can't be zero
        if s == 0 or m == 0:
            continue
        
        send = s*1000 + e*100 + n*10 + d
        more = m*1000 + o*100 + r*10 + e
        money = m*10000 + o*1000 + n*100 + e*10 + y
        
        if send + more == money:
            print(f"SOLUTION:")
            print(f" {send}")
            print(f"+{more}")
            print(f"-----")
            print(f"{money}")
            print(f"Mapping: {dict(zip(letters, perm))}")
            return

    print("No solution found.")

if __name__ == "__main__":
    solve_cryptarithmetic()
