from random import randint


fortunes = ['hello fortune!', 
            'party on wayne', 
            'your lucky number is 13',
            'you will have a great day tomorrow',
            'you will be glittered with gold']


def first_fortune():
    """Returns first item in list.

        >>> first_fortune()
        'hello fortune!'
    """
    
    return fortunes[0]

def all_fortunes():
    """Returns all fortunes in list.

        >>> all_fortunes()
        hello fortune!
        party on wayne
        your lucky number is 13
        you will have a great day tomorrow
        you will be glittered with gold
    """

    for fortune in fortunes:
        print fortune

def generate_random_num():
    """Generates a random number between 0 and length of fortune list.


    """
    return randint(0, len(fortunes) - 1)


def random_fortune():
    """Returns a random fortune from a list."""

    return fortunes[generate_random_num()]  






#####################################
if __name__ == "__main__":
    import doctest
    if doctest.testmod().failed == 0:
        print "Wooot! Test passed! Keep going!"
