def reverse(number):
    print("original number", number)
    original_num = number
    
    # reverse the given number
    reverse_num = 0
    reverse_num_sep = ''
    while number > 0:
        reminder = number % 10
        reverse_num = (reverse_num * 10) + reminder
        reverse_num_sep = reverse_num_sep + str(reminder)+'  '
        number = number // 10

    # check numbers
    
    print(reverse_num_sep)
    
reverse(1234)