""" File: AdvObject.py

    This module defines the AdvObject class which models an object 
    in the Adventure.
"""

class AdvObject:

    def __init__(self, name, description, location):
        """Creates an AdvObject from the specified properties.

        Args:
            name (str): the unique name of the object
            description (str): a short description of the object
            location (str): the name of the location where the object first appears
        """
        self._name = name
        self._description = description
        self._initlocation = location

    def __str__(self):
        """Converts an AdvObject to a string."""
        return self._name

    def get_name(self):
        """Returns the name of this object."""
        return self._name

    def get_description(self):
        """Returns the description of this object."""
        return self._description

    def get_initial_location(self):
        """Returns the initial location of this object."""
        return self._initlocation

# Method to read an object from a file

def read_object(f,start):
    """Reads the next object from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the opened object's text file
    Returns:
        (AdvObject or None): an AdvObject object or None if at end of the file
    """
    lines = f.readlines().copy()
    lines = [line.rstrip() for line in lines]
    try:
        name = lines[start]
        description = lines[start + 1]
        location = lines[start + 2]
    except:
        return None

    return AdvObject(name, description, location)  # Return the completed object