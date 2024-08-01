def converter(number, base):
    conversion = "0123456789ABCDEF"
    digit = number % base
    number = number // base
    temp = ""
    if number != 0:
        temp = converter(number, base)
    temp+= conversion[digit]
    return temp

print(converter(50,2))