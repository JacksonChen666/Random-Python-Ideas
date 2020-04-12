"""
This Module/Library generates random numbers and strings using the random and string module
"""


def setSeed(seed=None):
    """
    Uses the input to set the seed for the random module
    :param seed: The seed for the random module (Default is random)
    :return:
    """
    if seed is None:
        random.seed(random.randint(0,999999999))
    else:
        random.seed(seed)


def randomString(amount):
    """
    Generates random string from string.printable (Includes new lines etc.)
    :param amount: Amount of characters to generate (Default 10)
    :return:
    """
    temp = []
    if amount is None:
        amount = 10
    for i in range(amount):
        temp.append(random.choice(string.printable))


def randomLowercase(amount):
    """
    Generates random lowercase character(s)
    :param amount: Amount of characters to generate (Default 10)
    :return:
    """
    temp = []
    if amount is None:
        amount = 10
    for i in range(amount):
        temp.append(random.choice(string.lowercase))


def randomFullNumber(amount, min, max):
    """
    Generates random number(s) without decimal points
    :param min: Minimum number to generate
    :param max: Maximum number to generate
    :param amount: Amount of numbers to generate (Default 1)
    :return:
    """
    temp = []
    if min is None:
        min = 0
    if max is None:
        raise randomGenerator.MissingArgument("Missing argument: Maximum number")
    if amount is None:
        amount = 1
    for i in range(amount):
        temp.append(random.randint(min, max))


def randomDecimalNumber(amount, min, max):
    """
    Generates number(s) with decimal points
    :param min: Minimum number to generate
    :param max: Maximum number to generate
    :param amount: Amount of numbers to generate (Default 1)
    :return:
    """
    temp = []
    if min is None:
        min = 0
    if max is None:
        raise randomGenerator.MissingArgument("Missing argument: Maximum number")
    if amount is None:
        amount = 1
    for i in range(amount):
        temp.append(random.randint(min, max))


def __init__():
    """
    Initiation for the module
    :return:
    """
    global temp
    temp = []


__init__()
