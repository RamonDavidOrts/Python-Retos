def is_armstrong(num):
    str_num = str(num)
    res = 0
    for n in str_num:
        res += int(n)**len(str_num)
    return res == num
    
print(is_armstrong(371))
