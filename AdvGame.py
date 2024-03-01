""" File: AdvGame.py
    
    This module defines the AdvGame class, which records all information
    necessary to play a game.
"""

from AdvRoom import read_room
from AdvObject import read_object
from tokenscanner import TokenScanner
import random

class AdvGame:

    def __init__(self, prefix):
        """Reads the game data from files with the specified prefix and
        stores that information in attributes.

        Args:
            prefix (str): The prefix starting each of the file names
        Returns:
            None
        """
        # reading in objects
        self._objects = { }
        finished = False
        start = 0
        try:
            while not finished:
                with open(prefix + "/Objects.txt") as f:
                    object = read_object(f,start)
                    if object is None:
                        finished = True
                    else:
                        name = object.get_name()
                        self._objects[name] = object
                start += 4
        except:
            pass
        
        # reading in rooms
        with open(prefix + "/Rooms.txt") as f:
            self._rooms = { }
            finished = False
            while not finished:
                room = read_room(f,self._objects)
                if room is None:
                    finished = True
                else:
                    name = room.get_name()
                    if len(self._rooms) == 0:
                        self._rooms["START"] = room
                    self._rooms[name] = room

        # reading in synonyms
        self._synonyms = {}
        try:
            with open(prefix + "/Synonyms.txt") as f:
                lines = f.readlines()
                for line in lines:
                    if line != "":
                        equals = line.find("=")
                        self._synonyms[line[:equals]] = line[equals+1:-1]
        except:
            pass

        # creating inventory
        self._inventory = set()
        for value in self._objects.values():
            if value.get_initial_location() == "PLAYER":
                self._inventory.add(value)
        
    def get_room(self, name):
        """Returns the AdvRoom object with the specified name.
        Args:
            name (str): the unique name of a room
        Returns:
            (AdvRoom): the corresponding AdvRoom object
        """
        return self._rooms[name]
        
    def run(self):
        """Plays the adventure game stored in this object."""
        # print objects
        def print_objects(current):
                if self._rooms[current].get_contents() != None:
                    for value in self._rooms[current].get_contents().values():
                        print(f"There is {value.get_description()} here.")


        for line in HELP_TEXT:
            print(line)

        # start dialogue
        current = "START"
        show_room_message = True
        while current != "EXIT":

            room = self._rooms[current]
            if not room.is_entered():
                for line in room.get_long_description():
                    print(line)
                print_objects(current)
                room.set_entered()
            elif show_room_message is True:
                print(room.get_short_description())
                print_objects(current)

                # extension
                if random.random() < .05:
                    print("A mysterious traveler walks by without saying a word.")
                elif random.random() < .03:
                    print("A friendly travel walks by and waves at you.")
            else:
                show_room_message = True

            # getting input
            is_forced = False
            for passage in self._rooms[current].get_passages():
                if "FORCED" in passage:
                    is_forced = True
                    action_verb = "FORCED"
            
            if is_forced is False:
                response = input("> ").strip().upper()

                # separating action and motion verbs
                scanned_response = TokenScanner(response)
                action_verb = scanned_response.next_token()
                motion_verb = None
                scanned_response.next_token()

                if action_verb in self._synonyms:
                    action_verb = self._synonyms[action_verb]            
                if scanned_response.has_more_tokens():
                    motion_verb = scanned_response.next_token()
                    if motion_verb in self._synonyms:
                        motion_verb = self._synonyms[motion_verb]
                    if scanned_response.has_more_tokens():
                        action_verb = None

            # if response is QUIT
            if action_verb == "QUIT":
                print("Safe travels!")
                current = "EXIT"
            
            # if response is HELP
            elif action_verb == "HELP":
                for line in IN_GAME_HELP_TEXT:
                    print(line)
                    show_room_message = False

            # if response is LOOK
            elif action_verb == "LOOK":
                for line in room.get_long_description():
                    print(line)
                print_objects(current)
                show_room_message = False

            # if response is INVENTORY
            elif action_verb == "INVENTORY":
                if len(self._inventory) == 0:
                    print("You are empty-handed.")
                else:
                    print("You are carrying:")
                    for value in self._inventory:
                        print(f"  - {value.get_description()}")
                show_room_message = False

            # if response is TAKE
            elif action_verb == "TAKE":
                items = self._rooms[current].get_contents()
                if items != None:
                    if motion_verb in items:
                        print("Item added to inventory.")
                        self._inventory.add(items[motion_verb])
                        self._rooms[current].remove_object(motion_verb)
                    else:
                        print("This item is not present here.")
                else:
                    print("This item is not present here.")
                show_room_message = False

            # if response is DROP
            elif action_verb == "DROP":
                to_remove = []
                for value in self._inventory:
                    if motion_verb == str(value):
                        print("This item has been dropped.")
                        self._rooms[current].add_object(value)
                        to_remove.append(value)
                    else:
                        print("This item is not in your inventory.")
                for value in to_remove:
                    self._inventory.remove(value)
                show_room_message = False

            # checking for room change
            else:
                passages = room.get_passages()
                try:
                    locked_passage_potential = action_verb + "/locked"
                except:
                    locked_passage_potential = None
                if locked_passage_potential in passages:
                    next_room = passages.get(locked_passage_potential,None)
                    slash = next_room.find("/")
                    if next_room[slash+1:] in [item.get_name() for item in self._inventory]:
                        next_room = next_room[:slash]
                    else:
                        next_room = passages.get(action_verb, None)
                else:
                    next_room = passages.get(action_verb, None)
                if next_room is not None:
                    current = next_room
                    
                # for forced passages
                    current_passages = self._rooms[current].get_passages()
                    if "FORCED" in current_passages:
                        for line in self._rooms[current].get_long_description():
                            print(line)
                        for key in current_passages.keys():
                            locked_force_found = False
                            if "FORCED/" in key and key[7:] in self._inventory:
                                current = current_passages[key]
                                locked_force_found = True
                        if locked_force_found == False:
                            current = current_passages["FORCED"]
                            show_room_message = False
                        
                # if response is not possible
                else:
                    print("I cannot understand this request.")
                    show_room_message = False

# Constants

HELP_TEXT = [
    "Welcome to Adventure!",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.  Direct me with natural English commands; I don't understand",
    "all of the English language, but I do a pretty good job.",
    "",
    "It's important to remember that cave passages turn a lot, and that",
    "leaving a room to the north does not guarantee entering the next from",
    "the south, although it often works out that way.  You'd best make",
    "yourself a map as you go along.",
    "",
    "Much of my vocabulary describes places and is used to move you there.",
    "To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.",
    "I also know about a number of objects hidden within the cave which you",
    "can TAKE or DROP.  To see what objects you're carrying, say INVENTORY.",
    "To reprint the detailed description of where you are, say LOOK.  If you",
    "want to end your adventure, say QUIT.",
    "",
    ""
]

IN_GAME_HELP_TEXT = [
    "Hello, again! Once again, I will remind you of your quest:",
    "Somewhere nearby is Colossal Cave, where others have found fortunes in",
    "treasure and gold, though it is rumored that some who enter are never",
    "seen again.  Magic is said to work in the cave.  I will be your eyes",
    "and hands.",
    "Here are some commands to try out if you are stuck:",
    "   EAST:      Journey East      IN:        Go inside a location",
    "   WEST:      Journey West      OUT:       leave a location",
    "   NORTH:     Journey North     UP:        Travel up",
    "   SOUTH:     Journey South     DOWN:      Travel down",
    "   TAKE:      Take an item      DROP:      Drop an item",
    "   INVENTORY: Check inventory   HELP:      Request guidance",
    "   LOOK:      Look around       QUIT:      Quit game"
]