# Validating the Phone Number
# https://www.hackerrank.com/challenges/validating-the-phone-number/problem


import re

if __name__ == '__main__':
    N = int(input())
    for _ in range(N):
        phone_number = input()
        if re.match(r'^[789]\d{9}$', phone_number):
            print("YES")
        else:
            print("NO")