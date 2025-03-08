def swap_cases(s):
    x = ""
    for i in s:
        if i.isupper():
            x += i.lower()
        else:
            x += i.upper()
    return x


x = input("Enter string:")
print(swap_cases(x))
