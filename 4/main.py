INPUT = "278384-824795"
LOW = 278384
HIGH = 824795

def meets_criteria(num):
    string = str(num)
    return has_double_digits(string) and never_decreases(string)

def has_double_digits(str):
    for i in range(len(str) - 1):
        if str[i] == str[i+1]:
            return True
    return False

def never_decreases(str):
    for i in range(len(str) - 1):
        if str[i] > str[i+1]:
            return False
    return True

def main1():
    sum = 0
    for num in range(LOW, HIGH+1):
        sum += 1 if meets_criteria(num) else 0
    return sum

def meets_criteria_2(num):
    string = str(num)
    return never_decreases(string) and has_double_digits_2(string)

def has_double_digits_2(str):
    for i in range(len(str) - 1):
        if (str[i] == str[i+1]) and (i+2 >= len(str) or (str[i+1] != str[i+2])) and (i-1 < 0 or (str[i-1] != str[i])):
            return True
    return False

def main2():
    sum = 0
    for num in range(LOW, HIGH+1):
        sum += 1 if meets_criteria_2(num) else 0
    return sum

print(main1())
print(main2())
