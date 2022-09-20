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

def recursive_dec2bin(dec, newdec=None , bin=""):
    if newdec == None:
        newdec = abs(dec)
    if dec == 0:
        bin = "0"
    if newdec >= 1:
        bin = str(newdec % 2) + bin
        newdec = newdec // 2
        bin = recursive_dec2bin(dec, newdec, bin)
    elif dec < 0:
        bin = "-" + bin
    return bin

print(dec2bin(45678313))
print(recursive_dec2bin(45678313))
