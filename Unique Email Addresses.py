emails = ["test.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]
# emails = ["te.st.ema.il+alex@leetcode.com"]
email_new = []

for i in emails:
    i = i.split("@")
    k = i[0]
    k = list(k)
    for j in k:
        if j == '+':
            k = k[:k.index('+')]
            break
        if j == '.':
            k.pop(k.index('.'))
    k = ''.join(k)
    i[0] = k
    i = '@'.join(i)
    print(i)
    if i not in email_new:
        email_new.append(i)
print(email_new)










