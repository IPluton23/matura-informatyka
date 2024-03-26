file1 = open("sufiks_1.txt", "r")
file2 = open("slowa2.txt", "r")
file3 = open("slowa3.txt", "r")

def czy_mniejszy(n, s, k1, k2):
    i = k1
    j = k2
    while(i <= n and j <= n):
        if(s[i] == s[j]):
            i += 1
            j += 1
        else:
            if(s[i] < s[j]):
                return True
            else:
                return False
    if(j <= n):
        return True
    else:
        return False

file1.close()
file2.close()
file3.close()