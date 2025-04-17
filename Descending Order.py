def descending_order(num):
    return int("".join(sorted(str(num), reverse=True)))
print(descending_order(124789214719))

def descending_order_variant1(num):
    if num > 0:
        num_in_list = list(map(int, str(num)))
        num_in_list.sort(reverse=True)
        res = int("".join(map(str, num_in_list)))
        return res
    elif num == 0:
        return 0
    else:
        return  
print(descending_order_variant1(421421421))