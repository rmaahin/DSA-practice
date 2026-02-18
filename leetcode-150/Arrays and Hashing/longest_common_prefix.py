strs = ["flower","flow","flight"]

def longest_suffix(strs):
    prefix = strs[0]
    for s in strs:
        if len(s) < len(prefix):
            prefix = s

    for i in range(len(prefix)):
        for s in strs:
            if prefix[i] != s[i]:
                return prefix[:i]
    
    return prefix

res = longest_suffix(strs)
print(res)
