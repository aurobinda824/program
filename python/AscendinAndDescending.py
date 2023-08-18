m =[124, 45, 89, 67, 30, 200, 145, 765, 18, 0, 11]

def ascend(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] < n[j]:
                n[i], n[j] = n[j], n[i]
    return n

def descend(n):
    for i in range(len(n)):
        for j in range(len(n)):
            if n[i] > n[j]:
                n[i], n[j] = n[j], n[i]
    return n

print(ascend(m))
print(descend(m))
        