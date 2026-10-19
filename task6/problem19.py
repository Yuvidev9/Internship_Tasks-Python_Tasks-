# Company Logo
# https://www.hackerrank.com/challenges/company-logo/problem

from collections import Counter

if __name__ == '__main__':
    s = input().strip()
    
    # Count the occurrences of each character
    char_counts = Counter(s)
    
    # Sort characters:
    # 1. By frequency descending (-x[1])
    # 2. By character ascending alphabetically (x[0])
    sorted_chars = sorted(char_counts.items(), key=lambda x: (-x[1], x[0]))
    
    # Print the top 3 characters along with their occurrence count
    for char, count in sorted_chars[:3]:
        print(f"{char} {count}")
