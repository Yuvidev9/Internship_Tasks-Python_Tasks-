# String Validators
# https://www.hackerrank.com/challenges/string-validators/problem

if __name__ == '__main__':
    s = input()
    attributes = ['isalnum', 'isalpha', 'isdigit', 'islower', 'isupper'] 
    for att in attributes:
        method = getattr(str, att)
        print(any([method(a) for a in s]))