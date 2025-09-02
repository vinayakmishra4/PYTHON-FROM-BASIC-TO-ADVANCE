def print_n_to_1(n):
    # Base case: when n reaches 0, stop recursion
    if n == 0:
        return
    # Print current number
    print(n)
    # Recursive call with n-1
    print_n_to_1(n - 1)


# Example usage
num = int(input("Enter a number: "))
print_n_to_1(num)