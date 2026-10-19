# Collections.Counter()
# https://www.hackerrank.com/challenges/collections-counter/problem

if __name__ == '__main__':
    x = int(input())
    shoes = list(map(int, input().split()))
    n = int(input())
    
    shoe_counter = {}
    for shoe in shoes:
        shoe_counter[shoe] = shoe_counter.get(shoe, 0) + 1
    
    total_earnings = 0
    for _ in range(n):
        size, price = map(int, input().split())
        if shoe_counter.get(size, 0) > 0:
            total_earnings += price
            shoe_counter[size] -= 1
    
    print(total_earnings)