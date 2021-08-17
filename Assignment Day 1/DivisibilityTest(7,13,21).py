""" WAP to check whether the number is divisible by 7 or 13 or 21. """


def check(num):
    if num % 21 == 0:
        return 21
    elif num % 13 == 0:
        return 13
    elif num % 7 == 0:
        return 7
    else:
        return False


if __name__ == "__main__":
    # Give your input here
    n = 4
    if not check(n):
        print(f"{n} is not divisible by 7 or 13 or 21")
    else:
        d = check(n)
        print(f"{n} is divisible by {d}")
