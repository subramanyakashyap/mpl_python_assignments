def printMissingNum(n):
    nums = str(n)
    nums = list(map(int, nums))
    for i in range(10):
        if i not in nums:
            print(i)


if __name__ == "__main__":
    num = int(input("Enter the phone number"))
    printMissingNum(num)