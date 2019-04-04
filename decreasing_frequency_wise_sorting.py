from collections import Counter

a = list(map(int, input("Enter an array: ").split()))

# counts = Counter(a)
# n = sorted(a, key=lambda x: -counts[x])
# n = sorted(a, key=counts.get, reverse=True)
# n = sorted(a, key= lambda x:(counts[x], x), reverse=True)

d = {}
for i in a:
    if i in d:
        d[i] += 1
    else:
        d[i] = 1
print(d)

n = sorted(a, key=lambda x: -d[x])
print(n)
