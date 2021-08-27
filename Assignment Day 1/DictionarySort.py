""" WAP to sort dictionary by key or value in ascending order """


def sortByKey(dic):
    sortedDict = {}
    l = sorted(dic.keys())
    for i in l:
        sortedDict[i] = dic.get(i)
    return sortedDict


def sortByValue(dic):
    sortedDict = {}
    l = dic.keys()
    for i in l:
        sortedDict[i] = dic[i].upper()
    sortedDict = dict(sorted(sortedDict.items(), key=lambda kv: (kv[1], kv[0])))
    l = sortedDict.keys()
    for i in l:
        sortedDict[i] = dic.get(i)
    return sortedDict


if __name__ == "__main__":
    dit = {9: "Zzz", 10: "abc", 8: "Lol"}
    print(sortByKey(dit))
    print(sortByValue(dit))
