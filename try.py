person = 100
a = [0] * person
print(a)
for i in range(person):
    a[i] = i + 1
    print(a)
pos = 0
while len(a) > 1:
    pos += 1
    pos %= len(a)
    del a[pos]

print(a[0])


