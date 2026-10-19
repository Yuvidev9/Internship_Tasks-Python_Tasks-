# No Idea!
# https://www.hackerrank.com/challenges/no-idea/problem

if __name__ == '__main__':
    n, m = map(int, input().split())
    arr = list(map(int, input().split()))
    A = set(map(int, input().split()))
    B = set(map(int, input().split()))

    happiness_score = 0

    for element in arr:
        if element in A:
            happiness_score += 1
        elif element in B:
            happiness_score -= 1

    print(happiness_score)