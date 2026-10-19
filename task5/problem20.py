# Piling Up!
# https://www.hackerrank.com/challenges/piling-up/problem

from collections import deque

def check_stacking():
    # Read the number of test cases
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        # Store cube lengths in a double-ended queue
        cubes = deque(map(int, input().split()))
        
        # Initialize the top of the pile with a large number
        current_top = float('inf')
        possible = True
        
        while cubes:
            # Pick the larger cube from either end
            if cubes[0] >= cubes[-1]:
                picked = cubes.popleft()
            else:
                picked = cubes.pop()
            
            # If the picked cube is larger than the current top, stacking fails
            if picked > current_top:
                possible = False
                break
                
            current_top = picked
            
        if possible:
            print("Yes")
        else:
            print("No")

if __name__ == '__main__':
    check_stacking()
