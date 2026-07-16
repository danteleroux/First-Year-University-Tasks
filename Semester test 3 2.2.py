def reverse_striing(list):
    reverse_string = []
    index = len(list)-1
    length = 0
    while index >= 0:
        reverse_string.append(list[index])
        index -= 1
    return reverse_string

my_list = [1, 2, 3, 4, 5, 6]
reversed_list = reverse_striing(my_list)
print(reversed_list)
