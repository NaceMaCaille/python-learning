def high_and_low(numbers):
    maximum = str(max(int(elm) for elm in numbers.split())) 
    minimum = str(min(int(elm) for elm in numbers.split()))
    sum_str = maximum + " " + minimum
    return sum_str
print(high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))

def high_and_low_variant1(numbers):
    n = [int(elm) for elm in numbers.split(" ")]
    return f"{max(n)} {min(n)}"
print(high_and_low_variant1("8 3 -5 42 -1 0 0 -9 4 7 4 -4"))