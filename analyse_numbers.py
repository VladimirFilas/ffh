def is_even_number(number):
    if number %2 ==0:
        return True

    return False

def is_whole_number(number):
    if number %1 == 0 and number>=0:
        return True

    return False


my_numbers = [6,7,4,4,3,43,5,4,6]
for my_numbers in my_numbers:


print(is_even_number(my_numbers))
print(is_whole_number(my_numbers))


