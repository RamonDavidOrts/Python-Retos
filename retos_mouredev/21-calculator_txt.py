def is_float(element):
    try:
        float(element)
        return True
    except:
        return False
        
def calculator(file_name):
    file = open(file_name)
    result = None
    operator = None
    for index,line in enumerate(file, start=1):
        line = line.strip()
        index = str(index)
        if is_float(line):
            if result == None:
                result = float(line)
            elif operator != None:
                if operator == "+": result += float(line)
                elif operator == "-": result -= float(line)
                elif operator == "*": result *= float(line)
                elif operator == "/": result /= float(line)
                else: return "operator not valid: " + operator + " in line " + index
                operator = None
            else: return "not found operator between numbers in line " + index
        elif operator == None:
            operator = line
        else: return "not found number between operators in line " + index
    return result

print(calculator("operations.txt"))
