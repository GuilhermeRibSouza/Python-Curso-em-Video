import string

b20 = []
t = 0
c20 = 1
g = 0
n = int(input("Quantos termos da base 20 deseja ver? "))
for c in range(1, n+1):
    if c <= 10:
        b20.append(str(c-1))
        print(b20[c-1], end=' ')
    elif 10 < c <= 20:
        for a in range (ord('A')+ t, ord('B')+ t):
            b20.append(chr(a))
            print(b20[c-1], end = ' ')
            t += 1
    elif 20 < c:
        b20.append(str(c20) + str(b20[0+g]))
        print(b20[c-1], end = ' ')
        g += 1
        if c % 20 == 0:
            c20 += 1
        if g == 20:
            g = 0