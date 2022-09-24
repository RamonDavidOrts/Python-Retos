from datetime import datetime

def days_between(str1, str2):
    date1 = str2date(str1)
    date2 = str2date(str2)
    if (date1 and date2):
        delta = date2 - date1
        return abs(delta.days)
    else:
        return "Invalid date"

def str2date(str):
    try:
        return datetime.strptime(str, '%d/%m/%Y')
    except:
        try:
            return datetime.strptime(str, '%d/%m/%y')
        except:
            return None

print(days_between("25/02/2023", "24/09/2022"))
