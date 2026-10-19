# Introduction to Sets
# https://www.hackerrank.com/challenges/introduction-to-sets/problem

def average(array):
    # Convert the list to a set to remove duplicates
    unique_heights = set(array)
    
    # Calculate the sum of unique heights
    total_height = sum(unique_heights)
    
    # Calculate the average
    avg_height = total_height / len(unique_heights)
    
    return avg_height

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)