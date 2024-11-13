import sys

step = 0

def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 1:
        move_disk(from_rod, to_rod)
        print_step(f"Move disk 1 from rod {from_rod} to rod {to_rod}")
        return
    TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
    move_disk(from_rod, to_rod)
    print_step(f"Move disk {n} from rod {from_rod} to rod {to_rod}")
    TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

def move_disk(from_rod, to_rod):
    disk = rods[from_rod].pop()
    rods[to_rod].append(disk)

def print_rods_state():
    for i in range(n, 0, -1):
        row = []
        for rod in ['A', 'B', 'C']:
            if len(rods[rod]) >= i:
                row.append(f"{rods[rod][i-1]}  ")
            else:
                row.append("|  ")
        print("".join(row).rstrip())
    print("A  B  C")
    print()

def print_step(action):
    global step
    step += 1
    print(f"\n-->Step {step}: {action}")
    print_rods_state()

def get_positive_integer():
    while True:
        try:
            n = int(input("Enter the number of disks: "))
            if n <= 0:
                print("Please enter a positive integer.")
            else:
                return n
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

sys.setrecursionlimit(1500)

n = get_positive_integer()

rods = {
    'A': list(range(n, 0, -1)),
    'B': [],
    'C': []
}

print(f"\nTower of Hanoi Solution for {n} disks:")
print_rods_state()

# Start with the first move which will print the state after moving disk 1
TowerOfHanoi(n, 'A', 'C', 'B')

print(f"\nAll {n} disks have successfully moved from rod A to rod C")
