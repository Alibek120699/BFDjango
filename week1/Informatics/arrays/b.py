n = input()
inp = list(filter(lambda x: (int(x)%2 == 0), input().split()))

for i in inp:
	print(i, end=' ')