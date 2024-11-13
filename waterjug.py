from collections import deque

def Water_Jug_problem(X, Y, j1, j2, target):
    queue = deque()
    visited = set()  # To track visited states
    path = {}  # To store the path of jug states
    actions = {}  # To store the actions that lead to those states

    # Starting with both jugs empty
    queue.append((0, 0))
    visited.add((0, 0))
    path[(0, 0)] = None
    actions[(0, 0)] = None

    # BFS (Breadth-First Search)
    while queue:
        current = queue.popleft()
        current_j1, current_j2 = current

        # Check if either jug has reached the target
        if current_j1 == target or current_j2 == target:
            result_path = []
            while current:
                result_path.append(current)
                current = path[current]
            return result_path[::-1], actions  # Return the path and actions

        # All possible actions (production rules)
        next_states = [
            (X, current_j2, "Fill Jug1"),  # Fill Jug1
            (current_j1, Y, "Fill Jug2"),  # Fill Jug2
            (0, current_j2, "Empty Jug1"),  # Empty Jug1
            (current_j1, 0, "Empty Jug2"),  # Empty Jug2
            (current_j1 - min(current_j1, Y - current_j2), current_j2 + min(current_j1, Y - current_j2), "Pour Jug1 into Jug2"),  # Pour Jug1 into Jug2
            (current_j1 + min(current_j2, X - current_j1), current_j2 - min(current_j2, X - current_j1), "Pour Jug2 into Jug1")  # Pour Jug2 into Jug1
        ]

        # Iterate over all the next possible states
        for state in next_states:
            if state[:2] not in visited:  # Check if the state has been visited
                visited.add(state[:2])  # Mark as visited
                queue.append(state[:2])  # Add the state to the queue
                path[state[:2]] = current  # Record the path
                actions[state[:2]] = state[2]  # Record the action

    return None, actions  # Return None if no solution found

# Main Code
def positive(n):
    while True:
        try:
            value = int(input(n))
            if value <= 0:
                raise ValueError("Please enter positive values only.")
            return value
        except ValueError as e:
            print("Please enter positive values only.")

J1 = positive("Enter the volume of the first jug: ")
J2 = positive("Enter the volume of the second jug: ")
L = positive("Enter the target volume: ")

if J1 < L and J2 < L:
    print("Not possible. Both jugs are smaller than the target volume.")
else:
    print("Path is as follows:")
    path, actions = Water_Jug_problem(J1, J2, J1, J2, L)
    
    if path:
        for state in path:
            if state in actions and actions[state]:
                print(f"Action: {actions[state]}")
            print(f"Jug1: {state[0]}, Jug2: {state[1]}")
        print("Solution found.")
    else:
        print("No solution found.")
