""" WAP to sort dictionary by key or value in ascending order """


def sortByKey(dic):
    sortedDict = {}
    l = sorted(dic.keys())
    for i in l:
        sortedDict[i] = dic.get(i)
    return sortedDict


def sortByValue(dic):
    sortedDict = dict(sorted(dic.items(), key=lambda kv: (kv[1], kv[0])))
    return sortedDict


if __name__ == "__main__":
    dit = {9: "zzz", 4: "abc", 8: "lol"}
    print(sortByKey(dit))
    print(sortByValue(dit))
