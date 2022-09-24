def armstrong(num, index=None):
    str_num = str(num)
    if index == None:
        index = len(str_num) - 1
    res = int(str_num[index]) ** len(str_num)
    if index == 0:
        return res
    return res + armstrong(num, index - 1)

def is_armstrong(num):
    return num == armstrong(num)
    
print(is_armstrong(371))
