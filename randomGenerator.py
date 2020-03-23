import random
import string


# noinspection PyMethodFirstArgAssignment
class string(amount):
    """
    Random string generators
    """

    def randomString(self):
        """
        Generates random string from string.printable (Includes new lines etc.)
        :param self: Amount of characters to generate (Default 10)
        :return:
        """
        temp = []
        if self is None:
            self = 10
        for i in range(self):
            temp.append(random.choice(string.printable))

    def randomLowercase(self):
        """
        Generates random lowercase character(s)
        :param self: Amount of characters to generate (Default 10)
        :return:
        """
        temp = []
        if self is None:
            self = 10
        for i in range(self):
            temp.append(random.choice(string.lowercase))


# noinspection PyMethodFirstArgAssignment
class interger(amount, min, max):
    """
    Random number generators
    """

    def randomFullNumber(self, min, max):
        """
        Generates random number(s) without decimal points
        :param min: Minimum number to generate
        :param max: Maximum number to generate
        :param self: Amount of numbers to generate (Default 1)
        :return:
        """
        temp = []
        if min is None:
            min = 0
        if max is None:
            raise randomGenerator.MissingArgument("Missing argument: Maximum number")
        if self is None:
            self = 1
        for i in range(self):
            temp.append(random.randint(min, max))

    def randomDecimalNumber(self, min, max):
        """
        Generates number(s) with decimal points
        :param min: Minimum number to generate
        :param max: Maximum number to generate
        :param self: Amount of numbers to generate (Default 1)
        :return:
        """
        temp = []
        if min is None:
            min = 0
        if max is None:
            raise randomGenerator.MissingArgument("Missing argument: Maximum number")
        if self is None:
            self = 1
        for i in range(self):
            temp.append(random.randint(min, max))


def __init__():
    """
    Initiation for the module
    :return:
    """
    global temp
    temp = []


__init__()
