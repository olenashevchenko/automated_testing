a="We are not what we should be!\n We are not what we need to be.\n But at least we are not what we used to bе\n (Football Coach)"
b=a.split()
print(len(b))

import re
c=re.split(r'[!.\s\n()]', a)
d=''.join(c)
print(d)

for e in b:
    e = e.strip("!,().")
    print(e)

b.sort()
print(b)

f = {}
for g in b:
    g=g.strip("!,().")
    if g in f:
        f[g] = f[g] + 1
    else:
        f[g] = 1
print(f)