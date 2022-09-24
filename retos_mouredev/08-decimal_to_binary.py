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
        return 0
    if newdec is None:
        newdec = abs(dec)
    elif newdec < 1:
        if dec < 0:
            bin = "-" + bin
        return bin
    bin = str(newdec % 2) + bin
    newdec = newdec // 2
    return recursive_dec2bin(dec, newdec, bin)

print(dec2bin(45678313))
print(recursive_dec2bin(45678313))
