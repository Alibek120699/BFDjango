n = int(input())
ok = True

while n != 1:
	if n%2:
		ok = False
		break
	n /= 2

print('YES') if ok else print('NO')