ok = False

n = int(input())
inp = [int(x) for x in input().split()]
for i in range(1, n):
	if inp[i]*inp[i-1]>=0:
		ok = True
		break

res = 'YES' if ok else 'NO'
print(res)