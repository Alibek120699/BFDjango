def power_of_num(a, n):
	res = 1
	if n==0:
		return res
	for _ in range(n):
		res *= a
	return res

inp = [x for x in input().split()]
a = float(inp[0])
n = int(inp[1])
print(power_of_num(a, n))