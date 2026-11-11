# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self, name, birth):
        """Create a person with a name and date of birth."""
        if type(name) is not str:
            raise TypeError("Name must be a string")

        if name == "":
            raise ValueError("Name cannot be empty")

        if not isinstance(birth, date):
            raise TypeError("Birth must be a date object")

        self.name = name
        self.birth = birth
    # Implement methods initials() and is_birthday() here
    # (see README.md for further details)
    def initials(self):
        """Return the uppercase initials of the person's name."""
        return "".join(part[0].upper() for part in self.name.split())

    def is_birthday(self):
        """Return True if today is the person's birthday."""
        today = date.today()
        return (self.birth.month == today.month and
                self.birth.day == today.day)