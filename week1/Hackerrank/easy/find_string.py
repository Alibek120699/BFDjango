def count_substring(string, sub_string):
    res = 0
    n = len(string)
    k = len(sub_string)
    for i in range(n-k+1):
        if sub_string == string[i:i+k]:
            res += 1
    return res

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)