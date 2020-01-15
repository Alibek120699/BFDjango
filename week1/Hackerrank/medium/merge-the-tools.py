def merge_the_tools(string, k):
    # your code goes here
    subs = []
    for i in range(0, len(string)-k+1, k):
        subs.append(string[i:i+k])
    for i in range(k):
        subs[i] = subs[i][:i] + subs[i][i+1:]
    for i in subs:
        print(i)

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)