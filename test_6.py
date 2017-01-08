# Write a program which accepts a sequence of comma-separated numbers from
# console and generate a list and a tuple which contains every number.

new_list = []
item_list = input('Enter a list of numbers: ').split(',')
for x in item_list:
    new_list.append(x)
tuple_list = tuple(new_list)
print(new_list)
print(tuple_list)
