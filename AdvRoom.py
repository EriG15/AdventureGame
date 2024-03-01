""" File: AdvRoom.py

    This module defines the AdvRoom class which is responsible
    for modeling a single room in the Adventure.
"""

class AdvRoom:

    def __init__(self, name, text, passages, objects):
        """Creates a new room with the specified attributes.
        
        Args:
            name (str): the unique name of the room
            shortdesc (str): a short description of the room
            longdesc (list[str]): a list of strings making up a longer description
            passages (dict[str:str]): a dictionary of possible directions and
                corresponding room names
        Returns:
            None
        """
        self._name = name
        self._shortdesc = text[0]
        self._longdesc = text[1::]
        self._passages = passages
        self._entered = False
        self._objects = {}

        for obj in objects.values():
            if obj.get_initial_location() == name:
                self._objects[obj.get_name()] = obj

    def get_name(self):
        """Returns the name of this room."""
        return self._name

    def get_short_description(self):
        """Returns the one-line short description of this room.."""
        return self._shortdesc

    def get_long_description(self):
        """Returns the list of lines describing this room."""
        return self._longdesc

    def get_passages(self):
        """Returns the dictionary mapping directions to names."""
        return self._passages.copy()
    
    def is_entered(self):
        """Checks if the room has been entered before."""
        return self._entered

    def set_entered(self):
        """Sets the boolean for if the room has been entered to true."""
        self._entered = True

    def add_object(self,object):
        """Adds an object to the room."""
        self._objects[object.get_name()] = object

    def remove_object(self,object):
        """Removes an object to the room."""
        self._objects.pop(object)

    def contains_object(self,object):
        """Checks if the room contains an object."""
        if object in self._objects:
            return True
        else:
            return False

    def get_contents(self):
        """Returns objects that are in the room."""
        if len(self._objects) == 0:
            return None
        return self._objects.copy()


# Method to read a room from a file

def read_room(f,objects):
    """Reads the next room from the file, returning None at the end.

    Args:
        f (file handle): the file handle of the text file being read
    Returns:
        (AdvRoom or None): either an AdvRoom object or None if at end of file
    """
    # read name
    name = f.readline().rstrip()
    if name == "":
        return None

    # read text
    text = [ ]
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == "-----":
            finished = True
        else:
            text.append(line)

    # read passages
    passages = { }
    finished = False
    while not finished:
        line = f.readline().rstrip()
        if line == "":
            finished = True
        else:
            colon = line.find(":")
            if colon == -1:
                raise ValueError("Missing colon in " + line)
            response = line[:colon].strip().upper()
            next_question = line[colon + 1:].strip()
            if "/" in next_question:
                passages[response+"/locked"] = next_question
            else:
                passages[response] = next_question

    return AdvRoom(name, text, passages, objects)