def dec2bin(dec):
    bin = ""
    if dec == 0:
        bin = "0"
    while dec >= 1:
        bin = str(dec % 2) + bin
        dec = dec // 2
    return bin

def recursive_dec2bin(dec, bin=""):
    if dec >= 1:
        bin = str(dec % 2) + bin
        dec = dec // 2
        bin = recursive_dec2bin(dec, bin)
    return bin

print(dec2bin(45678313))
print(recursive_dec2bin(45678313))
