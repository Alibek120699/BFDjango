n = int(input())
inp = [int(x) for x in input().split()]

for i in range(n):
	if i%2 == 0:
		print(inp[i], end=' ')