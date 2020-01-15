n = int(input())
arr = set([int(x) for x in input().split()])
arr = sorted(arr)
if len(arr) == 1:
    print(arr[0])
else:
    print(arr[-2])
