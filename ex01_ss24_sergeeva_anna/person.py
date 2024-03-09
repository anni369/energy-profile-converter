class Person:
    def __init__(self, name: str):
        """constructor of Person class, takes and initialise internal/private '_name' attribute"""
        self._name = name

    @property
    def name(self) -> str:
        """getter for internal/private '_name' attribute"""
        return self._name


if __name__ == '__main__':
    """for testing purposes"""
    p = Person("Harald")
    print(p.name)

    # should raise an exception (uncomment to test manually):
    #p.name = "Schwab"
