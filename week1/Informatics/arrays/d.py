n = int(input())
inp = [int(x) for x in input().split()]
cnt = 0

for i in range(1, n):
	if inp[i]>inp[i-1]:
		cnt += 1

print(cnt)