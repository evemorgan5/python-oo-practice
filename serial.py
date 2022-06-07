class SerialGenerator:
    """Machine to create unique incrementing serial numbers.

    >>> serial = SerialGenerator(start=100)

    >>> serial.generate()
    100

    >>> serial.generate()
    101

    >>> serial.generate()
    102

    >>> serial.reset()

    >>> serial.generate()
    100
    """


# class SerialGenerator:

    def __init__(self,start = 100):
        """ Create generator to start at inital value of start -1 and
        set the current number to inital start value.
        Current number will be updated each time either method is run.
        """
        self.start = start - 1
        self.current_num = self.start

    def __repr__(self):
        return f"<SerialGenerator start={self.start}>"

    def generate(self):
        """ Adding 1 to current number each time generator method is run """
        self.current_num += 1
        return self.current_num

    def reset(self):
        """ Resetting current number to initial starting number """
        self.current_num = self.start







