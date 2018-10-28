from random import randint


fortunes = ['hello fortune!', 'party on wayne', 'your lucky number is 13']

def first_fortune():
    """Returns first item in list.

        >>> first_fortune()
        'hello fortune!'
    """
    
    return fortunes[0]

def all_fortunes():
    """Returns all fortunes in list.

        >>> return_all_fortunes()
        hello fortune!
        party on wayne
        your lucky number is 13
    """

    for fortune in fortunes:
        print fortune


def random_fortune():
    """Returns a random fortune from a list."""

    random_num = randint(0, len(fortunes) - 1)

    return fortunes[random_num]  






#####################################
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Wooot! Test passed! Keep going!"
