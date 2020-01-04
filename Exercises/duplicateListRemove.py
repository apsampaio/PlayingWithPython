# First Method
def remove_duplicate(list):
    for number in list:
        if list.count(number) > 1:
            while (list.count(number) > 1):
                list.remove(number)
    return list


# Second Method
def remove_duplicates(list):
    copy = []
    for number in list:
        if number not in copy:
            copy.append(number)
    return copy



my_list = [1,1,2,2,3,3,4,4,5,5,5,5,5,5]
print(remove_duplicate(my_list))
print(remove_duplicates(my_list))
        



