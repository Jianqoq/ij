# Mark Boady
# CS 172 - Maze Game
# Drexel University 2018


class Maze:
    # Inputs: Pointers to start room and exit room
    # Sets current to be start room
    def __init__(self, st=None, ex=None):
        self.__start = st

        self.__exit = ex

        self.__current = st

    # Return the room the player is in (current)
    def getCurrent(self):
        return self.__current

    # The next four methods all have the same idea
    # See if there is a room in the direction
    # If the direction is None, then it is impossible to go that way
    # in this case return false
    # If the direction is not None, then it is possible to go this way
    # Update current to the new room (move the player)
    # then return true so the main program knows it worked.
    def moveNorth(self):
        if self.__current.getNorth():
            self.__current = self.__current.getNorth()
            return True
        else:
            return False

    def moveSouth(self):
        if self.__current.getSouth():
            self.__current = self.__current.getSouth()
            return True
        else:
            return False

    def moveEast(self):
        if self.__current.getEast():
            self.__current = self.__current.getEast()
            return True
        else:
            return False

    def moveWest(self):
        if self.__current.getWest():
            self.__current = self.__current.getWest()
            return True
        else:
            return False

    # If the current room is the exit,
    # then the player won! return true
    # otherwise return false
    def atExit(self):
        return self.__current == self.__exit

    # If you get stuck in the maze, you should be able to go
    # back to the start
    # This sets current to be the start room
    def reset(self):
        self.__current = self.__start
