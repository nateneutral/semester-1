# Worksheet 1.5: Person class

from datetime import date

class Person:
    """
    A Person, with a name and a date of birth.
    """

    # Write a constructor here to create and initialize name and
    # birth fields (see README.md for further details)
    def __init__(self,name,birth):
        if not isinstance(name, str):
            raise TypeError("Name inputted is not a valid string")
        elif name == "":
            raise ValueError("Name inputted is empty")
        if not isinstance(birth, date):
            raise TypeError("birthdate inputted is not a valid date")
        self.Name = name
        self.birth = birth
    
    # Implement methods initials() and is_birthday() here
    def initials(self):
        """
        returns first letter of each name in self.name
        returns: i (string)
        """
        names = [n.strip() for n in self.Name.split(" ")]
        i =""
        i = [n[0].upper() for n in names]
        ini =""
        for c in i:
            ini += c
        return(ini)
    def is_birthday(self):
        """
        compares the birthday of person and the current date and determines whether they match.
        returns: bool
        """
        today = date.today()
        if self.birth == today:
            return(True)
        return(False)
    # (see README.md for further details)
birthdate = date(2007, 8, 7)
keir = Person("Keiran michael William hearn",birthdate)
print(keir.initials())
print(keir.is_birthday())