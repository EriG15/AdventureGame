# Conway's Game of Life

A fantasy adventure game. 

## Description

Invented by William Crowther, this text-based game titled Colossal Cave Adventure pioneered the adventure game genre, captivating players with its immersive storytelling and puzzles. 

## Getting Started

### Relevant Modules

* `./Adventure.py`: This module calls an instance of the AdvGame class, passing in the game mode as a parameter.
* `./AdvGame.py`: This module holds the AdvGame class which runs and progresses the game.
* `./AdvObject.py`: This module holds the AdvObject class which is used to represent an object in AdvGame.
* `./AdvRoom.py`: This module holds the AdvRoom class which is used to represent a room in AdvGame.
* `./Crowther/`: This folder holds the relevant data for Crowther's 77-room adventure.
* `./Small/`: This folder holds the relevant data for the smaller 12-room adventure.
* `./tokenscanner.py`: This module implements a token scanner which is used to parse an input for the game.

### Dependencies

* Python 3.11.3 (recommended version)

### Installing and Executing

* Clone this repository to get this program.
* Navigate to the repository using command prompt or a code editor.
* Run `python -m Adventure.py`

## Playing the Game

The player's story begins as they are prompted with the following text:
```
Welcome to Adventure!
Somewhere nearby is Colossal Cave, where others have found fortunes in
treasure and gold, though it is rumored that some who enter are never
seen again.  Magic is said to work in the cave.  I will be your eyes
and hands.  Direct me with natural English commands; I don't understand
all of the English language, but I do a pretty good job.

It's important to remember that cave passages turn a lot, and that
leaving a room to the north does not guarantee entering the next from
the south, although it often works out that way.  You'd best make
yourself a map as you go along.

Much of my vocabulary describes places and is used to move you there.
To move, try words like IN, OUT, EAST, WEST, NORTH, SOUTH, UP, or DOWN.
I also know about a number of objects hidden within the cave which you
can TAKE or DROP.  To see what objects you're carrying, say INVENTORY.
To reprint the detailed description of where you are, say LOOK.  If you
want to end your adventure, say QUIT.

You are standing at the end of a road before a small brick
building.  A small stream flows out of the building and
down a gully to the south.  A road runs up a small hill
to the west.
>
```
With the last paragraph in the introduction, the player learns of their current surroundings. From here, they can type in commands to move around. In this case, these commands are `IN`, `SOUTH` and `WEST`, however that may be different for another location.
<br>
As the player continues to use commands to navigate and discover the world, they might come across different objects like a set of keys or a lamp. These objects are essential for completion of the game. In order to take an object you will simply use the `TAKE` command; for example, `TAKE KEYS` would be used to take a set of keys. These objects can additionally be dropped with the `DROP` command. Based on what objects you have in your inventory you may be able to get into certain rooms which you otherwise may not be able to. Below is a sequence of commands which one might use while playing the game:
```
You are standing at the end of a road before a small brick
building.  A small stream flows out of the building and
down a gully to the south.  A road runs up a small hill
to the west.
> SOUTH
You are in a valley in the forest beside a stream tumbling
along a rocky bed.  The stream is flowing to the south.
> SOUTH
At your feet all the water of the stream splashes into a
two-inch slit in the rock.  To the south, the streambed is
bare rock.
> SOUTH
You are in a 20-foot depression floored with bare dirt.
Set into the dirt is a strong steel grate mounted in
concrete.  A dry streambed leads into the depression from
the north.
> DOWN
The grate is locked and you don't have any keys.
> NORTH
Slit in rock
> NORTH
Valley beside a stream
> NORTH
Outside building
> IN
You are inside a building, a well house for a large spring.
The exit door is to the south.  There is another room to
the north, but the door is barred by a shimmering curtain.
There is a set of keys here.
> TAKE KEYS
Item added to inventory.
> SOUTH
Outside building
> SOUTH
Valley beside a stream
> SOUTH
Slit in rock
> SOUTH
Outside grate
> DOWN
You are in a small chamber beneath a 3x3 steel grate to
the surface.  A low crawl over cobbles leads inward to
the west.
There is a brightly shining brass lamp here.
>
```
The player will keep exploring until they reach the end of the game or die before doing so.

## Custom Worlds

With the design seen in the game text files, it is not too difficult for a user to make their own adventures to play in.

## Authors

Erik Griswold - Responsible for the Development of `Adventure.py`, `AdvGame.py`, `AdvObject.py` and `AdvRoom.py`.

William Crowther - Responsible for the idea of the adventure game and the design of the 77-room game.

Jed Rembold & Fred Agbo - Developers of the `tokenscanner.py` and the simplified 12-room game.