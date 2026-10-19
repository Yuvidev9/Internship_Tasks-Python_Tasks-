# Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem


def average(array):
    s = set(array) 
    length = len(s) 
    total = sum(s)
    
    arr = total/length
    return arr

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)