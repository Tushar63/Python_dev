def count(pat, txt):
    M = len(pat)
    N = len(txt)
    res = 0
     
    for i in range(N - M + 1):
         
        j = 0
        while j < M:
            if (txt[i + j] != pat[j]):
                break
            j += 1
        
        if (j == M):
            res += 1
            j = 0
    return res
     
if __name__ == '__main__':
    txt = input("enter the main string: ")
    pat = input("enter the substring to be found in main string: ")
    print(count(pat, txt))