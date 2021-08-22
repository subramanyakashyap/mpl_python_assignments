def fact(n):
    if n == 0 or n == 1:
        return 1
    return n * fact(n - 1)


def count(n):
    nums = str(n)
    nums = list(map(int, nums))
    end = len(nums) - 1
    c = 0
    while nums[end] == 0 and end != 0:
        c += 1
        end -= 1
    return c


if __name__ == "__main__":
    num = int(input("Enter a number: "))
    fact_n = fact(num)
    print("No of Zeroes: ", count(fact_n))
