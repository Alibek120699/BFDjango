import sys

res = 0
for lines in sys.stdin:
	for i in lines.split():
		res += int(i)

print(res)