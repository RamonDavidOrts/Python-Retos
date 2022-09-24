def dec2bin(dec):
    bin = ""
    newdec = abs(dec)
    if dec == 0:
        bin = "0"
    while newdec >= 1:
        bin = str(newdec % 2) + bin
        newdec = newdec // 2
    if dec < 0:
        bin = "-" + bin
    return bin

def recursive_dec2bin(dec, newdec=None, bin=""):
    if dec == 0:
        return "0"
    if newdec == 1:
        if dec < 0:
            return "-1"
        return "1"
    if newdec == None:
        newdec = abs(dec)
    return recursive_dec2bin(dec, newdec // 2) + str(newdec % 2)

print(dec2bin(45678313))
print(recursive_dec2bin(45678313))
