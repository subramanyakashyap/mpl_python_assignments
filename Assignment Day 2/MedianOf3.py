def findMedian(a):
    a.sort()
    return a[1]


if __name__ == "__main__":
    n1 = int(input("Enter first number: "))
    n2 = int(input("Enter second number: "))
    n3 = int(input("Enter third number: "))
    print("Median:", findMedian([n1, n2, n3]))
