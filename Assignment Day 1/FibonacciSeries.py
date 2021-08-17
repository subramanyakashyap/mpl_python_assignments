""" WAP to print fibonacci series using recursion between n1 and n2 (n1 and n2 should be user inputs) """


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == "__main__":
    n1 = int(input("Enter the value for n1\n"))
    n2 = int(input("Enter the value for n2\n"))
    print(f"The Fibonacci series from {n1} to {n2} is:")
    for i in range(n1, n2):
        print(fibonacci(i), end="  ")
