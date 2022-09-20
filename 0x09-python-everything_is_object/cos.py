l1 = [1, 2, 3]
l2 = l1
print(l2 is l1)
l1 = l1 + [4]
print(l2 is l1)
print(l2)

def increment(n):
    n += 1

a = 1
increment(a)
print(a)


copy_list = __import__('19-copy_list').copy_list

my_list = [1, 2, 3]
print(my_list)

new_list = copy_list(my_list)

print(my_list)
print(new_list)

print(new_list == my_list)
print(new_list is my_list)
