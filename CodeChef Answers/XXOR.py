n, q = list(map(int, input().split()))
n_numbers = list(map(int, input().split()))


def binaryToDecimal(binary):
    decimal, i, n = 0, 0, 0
    while(binary != 0):
        dec = binary % 10
        decimal = decimal + dec * pow(2, i)
        binary = binary//10
        i += 1
    return decimal

for _ in range(q):
    l, r = list(map(int, input().split()))
    bin_n_numbers = []
    max_len = 0
    
    for i in n_numbers[l-1: r]:
        temp = bin(i)
        bin_n_numbers.append(temp[2:])
        length_temp = len(temp[2:])
        if max_len < length_temp:
            max_len = length_temp
    
    for j in bin_n_numbers:
        j_length = len(j)
        if j_length < max_len:
            bin_n_numbers[bin_n_numbers.index(j)] = (max_len - j_length)*"0" + j
    ans = ""
    for k in range(max_len):
        zeros = 0
        ones = 0
        for h in range(len(bin_n_numbers)):
            if bin_n_numbers[h][k] == "0":
                zeros += 1
            else:
                ones += 1
        if zeros < ones:
            ans += "0"
        elif ones < zeros:
            ans += "1"
        else:
            ans += "0"
    ans = ((31-len(ans))*"1") + ans
    ans = int(ans)
    print(binaryToDecimal(ans))
    
