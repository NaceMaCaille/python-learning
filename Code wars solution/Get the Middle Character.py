def get_middle_variant0(s):
    index ,odd = divmod(len(s),2)
    return s[index] if odd else s[index -1 : index + 1]

#If the string length is odd, return the middle character.
print(get_middle_variant0("abcab"))

#If the string length is even, it will return 2 middle characters.
print(get_middle_variant0("abcabc"))

def get_middle_variant1(s):
    if len(s) % 2 != 0:
        mid = len(s) // 2
        res = s[mid]
        return res
    else:
        mid = len(s) // 2
        res = s[mid -1 : mid + 1]
        return res
#If the string length is odd, return the middle character.
print(get_middle_variant1("apple"))

#If the string length is even, it will return 2 middle characters.
print(get_middle_variant1("banana"))

def get_middle_variant2(s):
    x = len(s)
    y = int(x/2)
    if x % 2 == 0:
        return s[y -1: y + 1]
    else:
        return s[y:y + 1]
print(get_middle_variant2("chery"))

print(get_middle_variant2("pinapple"))

def get_middle_variant3(s):
    y = (len(s) - 1) // 2
    return s[y: -y] or s
print(get_middle_variant3("testing"))

print(get_middle_variant3("ice"))

def get_middle_variant4(s):
    return s[(len(s) -1) // 2 : (len(s) + 2) // 2]
print(get_middle_variant4("Opera"))
print(get_middle_variant4("Google"))