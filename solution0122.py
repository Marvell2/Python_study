n = int(input())
n1 = n % 10
n2 = n // 10 % 10
n3 = n // 100 % 10
n4 = n // 1000 % 10
if n1 == n4 and n2 == n3:
    print('1')
else:
    print('0')
