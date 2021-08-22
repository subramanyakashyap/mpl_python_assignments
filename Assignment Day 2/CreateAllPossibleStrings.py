from itertools import permutations


def printAllStrings(characters):
    for i in permutations(characters):
        print("".join(i))


if __name__ == "__main__":
    c = ['a', 'e', 'i', 'o', 'u']
    printAllStrings(c)