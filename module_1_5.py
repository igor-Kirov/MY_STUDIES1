mmutable_var=(1, "String", True, 0.56)
print('Immutable tuple: ',mmutable_var)
#mmutable_var[2]=False TypeError: 'tuple' object does not support item assignment
mutable_list = [1, "String", True, 0.56]
print('Mutable list: ', mutable_list)
mutable_list[2]=False
mutable_list[0]=23
print('Modified Mutable list: ', mutable_list)