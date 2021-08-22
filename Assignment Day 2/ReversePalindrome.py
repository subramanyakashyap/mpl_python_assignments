def reverse(n):
    rev = 0
    while n > 0:
        dig = n % 10
        rev = rev * 10 + dig
        n = n // 10
    return rev


isPalindrome = lambda n: True if n == reverse(n) else False

if __name__ == "__main__":
    for i in range(100, 10000):
        n = i + reverse(i)
        if isPalindrome(n):
            print(i, ": True")
