""" WAP to print below pattern:

	* * * * *
	 * * * *
	  * * *
	   * *
	    *
	   * *
	  * * *
	 * * * *
	* * * * * """


def pattern(n):
    k = 1
    for i in range(n, 0, -1):
        for j in range(k, 0, -1):
            print(end=" ")
        k += 1
        for j in range(0, i):
            print("*", end=" ")
        print()
    for i in range(0, n - 1):
        for j in range(0, k - 2):
            print(end=" ")
        k -= 1
        for j in range(i + 2, 0, -1):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    pattern(5)
