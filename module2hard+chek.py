spisok_right = ['12', '13', '1423', '121524',
                '162534', '13172635', '1218273645',
                '141923283746', '11029384756', '12131511124210394857',
                '112211310495867', '1611325212343114105968', '1214114232133124115106978',
                '1317115262143531341251161079', '11621531441351261171089', '12151811724272163631545414513612711810',
                '118217316415514613712811910', '13141911923282183731746416515614713812911']
otv = []
for n in range(3, 21):
    kod = []
    for i in range(1, n - 1):
        for j in range(i + 1, n):
            if n % (i + j) == 0:
                kod.append(str(i))
                kod.append(str(j))
    otv.append(''.join(kod))
    print(n, ''.join(kod))
print(spisok_right == otv)
