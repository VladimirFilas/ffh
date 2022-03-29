def is_even_number(number):
    if number %2 ==0:
        return True

    return False

def is_whole_number(number):
    if number %1 == 0 and number>=0:
        return True

    return False

my_number = 5
print(is_even_number(my_number))
print(is_whole_number(my_number))


