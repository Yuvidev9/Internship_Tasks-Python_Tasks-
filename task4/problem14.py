# Set .add()
# https://www.hackerrank.com/challenges/set-add/problem

if __name__ == '__main__':
    n = int(input())
    s = set()
    
    for _ in range(n):
        s.add(input().strip())
    
    print(len(s))