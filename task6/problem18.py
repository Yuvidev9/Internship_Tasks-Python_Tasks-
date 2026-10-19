# Set Mutations
# https://www.hackerrank.com/challenges/py-set-mutations/problem

if __name__ == '__main__':
    n = int(input())
    A = set(map(int, input().split()))
    m = int(input())
    for _ in range(m):
        operation = input().split()
        B = set(map(int, input().split()))
        if operation[0] == 'update':
            A.update(B)
        elif operation[0] == 'intersection_update':
            A.intersection_update(B)
        elif operation[0] == 'difference_update':
            A.difference_update(B)
        elif operation[0] == 'symmetric_difference_update':
            A.symmetric_difference_update(B)
    print(sum(A))