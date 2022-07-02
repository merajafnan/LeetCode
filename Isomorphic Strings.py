s = 'foo'
t = 'bar'
s1 = list(s)
t1 = list(t)
z1 = []
for i in range(0,len(t1)-1):
    if t1[i] != s1[i] and t1[i] not in z1:
        for j in range(0,len(s1)-1):
            if t1[i] == s1[j]:
                s1[j] = t1[i]
        z1.append(t1[i])
print(s1)






