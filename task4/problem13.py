# Symmetric Difference
# https://www.hackerrank.com/challenges/symmetric-difference/problem

if __name__ == '__main__':
    m = int(input())
    set_m = set(map(int, input().split()))
    
    n = int(input())
    set_n = set(map(int, input().split()))
    
    # Calculate the symmetric difference
    symmetric_diff = set_m.symmetric_difference(set_n)
    
    # Print the sorted result
    for num in sorted(symmetric_diff):
        print(num)