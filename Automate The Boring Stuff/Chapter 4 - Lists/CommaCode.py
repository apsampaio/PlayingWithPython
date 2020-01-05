spam = ['apples', 'cats', 'bananas']


def list_value(list):
    if list == []:
        return "Empty List"
    if len(list) == 1:
        return list[0]
    word = ""
    for x in range(len(list)):
        if x == len(list) - 1:
            word += 'and '
            word += list[x]
            return word
        else:
            word += list[x]
            word += ", "


print(list_value(spam))
print(list_value([]))
