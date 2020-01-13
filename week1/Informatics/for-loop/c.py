a = int(input())
b = int(input())
for i in range(a, b+1):
	if int(i ** 0.5) == i ** 0.5:
		print(i, end=' ')