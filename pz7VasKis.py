def nikita_kravchenko_spisyvaet_need_to_otchislit(list):
    otric = max(list)
    if otric<0:
        return otric
    cymma = 0
    konec = 0
    for i in (list):
        konec = konec + i
        konec = max(konec, 0)
        cymma = max(cymma, konec)
    return cymma


n = int(input())
a = [0]*n
for i in range(0, n):
    a[i] = int(input())
print(a)
print(nikita_kravchenko_spisyvaet_need_to_otchislit(a))





