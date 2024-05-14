def get_number_racers():

    while True:
        racers = input('Enter number of racers (2-4): ')
        if racers.isdigit():
            racers = int(racers)
        else:
            print('PLEASE enter a digit ....')
            continue

        if 2 <= racers <=4:
            return racers
        else:
            print('Enter a racers into the 2-4 ...')

racers = get_number_racers()