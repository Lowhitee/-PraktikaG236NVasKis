def tribonacci(n):
    if n in (1, 2):
        return 0
    if n in (3,):
        return 1
    return tribonacci(n - 1) + tribonacci(n - 2) + tribonacci(n - 3)

n = int(input())
a = [0]*n
b = [0]*n
for i in range(0, n):
    a[i] = int(input())
for i in range(0, n):
    b[i] = tribonacci(a[i])
print(a)
print(b)
