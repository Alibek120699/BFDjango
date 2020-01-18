def check(x):
	for i in range(2, int(x**0.5)+1):
		if x%i==0:
			return False
	return True

n = int(input())
d, p, ans = 2, 1, 1
while n!=1:
	if check(n)==True:
		if n==d:
			p += 1
		else:
			ans *= p
			p = 2
		break
	if n%d==0:
		n /= d
		p += 1
	else:
		ans *= p
		p = 1
		d += 1
print(ans*p)