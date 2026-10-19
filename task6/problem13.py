# Set .union() Operation
# https://www.hackerrank.com/challenges/py-set-union/problem

if __name__ == '__main__':
    n = int(input())
    english = set(map(int, input().split()))
    m = int(input())
    french = set(map(int, input().split()))
    print(len(english.union(french)))