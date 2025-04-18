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