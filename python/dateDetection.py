import re
def dateDetection(string):
    match = re.search(r'(\d{,2})\/(\d{,2})\/(\d{4})',string)
    if match == None:
        return None
    day = int(match.group(1))
    month = int(match.group(2))
    year = int(match.group(3))
    return day,month,year
def dateValidation(day,month,year):
    leapYear = False
    if month >12 or month <0 or day >31 or day <0:
        return "invalid date."
    if year %4==0:
        if year%100!=0:
            leapYear =True
        elif year%400 == 0:
            leapYear = True
    if leapYear and month==2:
        if day>29 :
            return "invalid date"
    return "valid"