# Using hashmaps

s = "anagram"
t = "nagaram"

# hashmap_s = {}
# hashmap_t = {}
# if len(s) == len(t):
#     for i in range(len(s)):
#         hashmap_s[s[i]] = s.count(s[i])
#         hashmap_t[t[i]] = t.count(t[i])

# if hashmap_s == hashmap_t:
#     print(True)
# else:
#     print(False)

# s_sorted = sorted(s)
# t_sorted = sorted(t)
# if s_sorted == t_sorted:
#     print(True)
# else:
#     print(False)

s = "anagram"
t = "nagaram"
hashmap_s = {}
hashmap_t = {}
if len(s) == len(t):
    for i in range(len(s)):
        hashmap_s[s[i]] = s.count(s[i])
        hashmap_t[t[i]] = t.count(t[i])

if hashmap_s == hashmap_t:
    print(True)

else:
    print(False)
