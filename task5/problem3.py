# Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

def mutate_string(string, position, character):
    # Convert the string to a list to make it mutable
    string_list = list(string)
    # Replace the character at the specified position
    string_list[position] = character
    # Join the list back into a string
    return "".join(string_list)

# def mutate_string(string, position, character):
#     return string[:position] + character + string[position + 1:]


if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)