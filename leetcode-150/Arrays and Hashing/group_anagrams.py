from collections import defaultdict

strs = ["act","pots","tops","cat","stop","hat"]

def group_anagrams(strs):
    grouped = defaultdict(list)
    for s in strs:
        temp = [0]*26
        for char in s:
            temp[ord(char) - ord('a')] += 1
        # print(temp)
        grouped[str(temp)].append(s)
    return (grouped)

res = group_anagrams(strs)
print(res.values())
