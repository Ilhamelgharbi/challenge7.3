dict2 = {
    "d": 4,
    "e": 5,
    "f": 6,
    "b": 2,
    "c": 3
}
items = list(dict2.items())
n = len(items)
for i in range(n):
    min_idx = i
    for j in range(i+1, n):
        if items[j][1] < items[min_idx][1]:
            min_idx = j
    items[i], items[min_idx] = items[min_idx], items[i]

dict_trie = dict(items)

for key, value in dict_trie.items():
    print(f"{key}: {value}")
