from random import randint

n = randint(3, 20)
kod = []
for i in range(1, n - 1):
    for j in range(i + 1, n):
        if n % (i + j) == 0:
            kod.extend([str(i), str(j)])
print(n, ''.join(kod))