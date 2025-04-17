def filter_list_variant0(l):
    return [elm for elm in l if not isinstance(elm,str)]
print(filter_list_variant0([1, 2, 'a', 'b']))

def filter_list_variant1(l):
    return [elm for elm in l if isinstance(elm,int)]
print(filter_list_variant1([1, 2, 'a', 'b']))

def filter_list_variant2(l):
    return [elm for elm in l if type(elm) == int]
print(filter_list_variant2([1, 2, 'a', 'b']))

def filter_list_variant3(l):
    return list(filter(lambda elm: isinstance(elm,int), l))
print(filter_list_variant3([1, 2, 'a', 'b']))