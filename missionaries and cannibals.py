from collections import deque

# Function to check if a state is valid
def is_valid(state, total_missionaries, total_cannibals):
    lM, lC, rM, rC = state
    if lM < 0 or lC < 0 or rM < 0 or rC < 0:  # No negative values allowed
        return False
    if lM > total_missionaries or lC > total_cannibals or rM > total_missionaries or rC > total_cannibals:  # Must be within bounds
        return False
    if (lM > 0 and lC > lM) or (rM > 0 and rC > rM):  # Cannibals cannot outnumber missionaries on either side
        return False
    return True

# Function to check if the goal state has been reached
def is_goal(state, total_missionaries, total_cannibals):
    _, _, rM, rC = state
    return rM == total_missionaries and rC == total_cannibals

# Function to get the possible next states based on boat capacity
def get_next_states(state, boat_on_left, total_missionaries, total_cannibals, boat_capacity):
    lM, lC, rM, rC = state
    next_states = []
    
    for m in range(0, boat_capacity + 1):
        for c in range(0, boat_capacity + 1):
            if m + c > 0 and m + c <= boat_capacity:  # At least 1 person but no more than boat capacity
                if boat_on_left:
                    if lM >= m and lC >= c:  # Move from left to right
                        next_states.append((lM - m, lC - c, rM + m, rC + c))
                else:
                    if rM >= m and rC >= c:  # Move from right to left
                        next_states.append((lM + m, lC + c, rM - m, rC - c))
    
    return [state for state in next_states if is_valid(state, total_missionaries, total_cannibals)]

# BFS to find the solution
def solve_missionaries_and_cannibals(total_missionaries, total_cannibals, boat_capacity):
    initial_state = (total_missionaries, total_cannibals, 0, 0)  # All missionaries and cannibals are on the left side
    boat_on_left = True  # Boat starts on the left side
    queue = deque([(initial_state, boat_on_left, [])])  # Store state, boat position, and path
    visited = set()  # Track visited states
    
    while queue:
        current_state, boat_on_left, path = queue.popleft()
        
        if is_goal(current_state, total_missionaries, total_cannibals):
            return path + [(current_state, boat_on_left)]
        
        if (current_state, boat_on_left) in visited:
            continue
        
        visited.add((current_state, boat_on_left))
        next_states = get_next_states(current_state, boat_on_left, total_missionaries, total_cannibals, boat_capacity)
        
        for next_state in next_states:
            queue.append((next_state, not boat_on_left, path + [(current_state, boat_on_left)]))
    
    return None  # No solution found

# Function to describe the changes in a state transition
def describe_step(current_state, next_state, boat_on_left):
    cM, cC, _, _ = current_state
    nM, nC, _, _ = next_state
    
    missionaries_moved = abs(cM - nM)
    cannibals_moved = abs(cC - nC)
    
    if boat_on_left:
        direction = "from left to right"
    else:
        direction = "from right to left"
    
    description = f"Moved {missionaries_moved} missionary(ies) and {cannibals_moved} cannibal(s) {direction}."
    
    return description

# Main function to run the solution and print the path
def print_solution(total_missionaries, total_cannibals, boat_capacity):
    solution = solve_missionaries_and_cannibals(total_missionaries, total_cannibals, boat_capacity)
    
    if solution:
        print(f"Initial state:\nLeft: M:{total_missionaries}, C:{total_cannibals}, B:1 | Right: M:0, C:0, B:0")
        print(f"Solution path for {total_missionaries} Missionaries, {total_cannibals} Cannibals, and Boat capacity {boat_capacity}:\n")
        for i in range(len(solution) - 1):
            current_state, boat_on_left = solution[i]
            next_state, _ = solution[i + 1]
            lM, lC, rM, rC = current_state
            
            # Print the state along with the boat status
            boat_status_left = "B:1" if boat_on_left else "B:0"
            boat_status_right = "B:0" if boat_on_left else "B:1"
            
           # print(f"Step {i + 1}:")
            print(f"Left: M:{lM}, C:{lC}, {boat_status_left} | Right: M:{rM}, C:{rC}, {boat_status_right}")
            print()
            
            # Print the description of the move
            description = describe_step(current_state, next_state, boat_on_left)
            print(f"Step {i + 1}:")
            print(description)
            #print()
        
        # Print the final state
        final_state, boat_on_left = solution[-1]
        lM, lC, rM, rC = final_state
        boat_status_left = "B:1" if boat_on_left else "B:0"
        boat_status_right = "B:0" if boat_on_left else "B:1"
        
        print(f"Left: M:{lM}, C:{lC}, {boat_status_left} | Right: M:{rM}, C:{rC}, {boat_status_right}")
        
        print("\nSolution found")
    else:
        print("No solution found.")

# Function to get a valid positive integer input
def get_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Invalid input. Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a valid number.")

# Main execution
if __name__ == "__main__":
    # Get user input for number of missionaries, cannibals, and boat capacity
    missionaries = get_positive_integer("Enter the number of missionaries: ")
    cannibals = get_positive_integer("Enter the number of cannibals: ")
    boat_capacity = get_positive_integer("Enter the boat capacity: ")
    
    # Print the solution path
    print_solution(missionaries, cannibals, boat_capacity)
