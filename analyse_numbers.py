def is_whole_number(number):
    if number %1 == 0 and number>=0:
        return True

    return False

my_number = 5
print(is_whole_number(my_number))
