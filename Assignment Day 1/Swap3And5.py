""" WAP to swap 3rd and 5th elements in a list. """


def swap3And5(lis):
    if len(lis) >= 5:
        lis[2], lis[4] = lis[4], lis[2]
        return lis
    else:
        print("Insufficient data")


if __name__ == "__main__":
    a = [1, 2, 3, 4, 5, 6, 7]
    print("List before swapping 3rd and 5th element:\n", a)
    a = swap3And5(a)
    if a is not None:
        print("List after swapping 3rd and 5th element:\n", a)
