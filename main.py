# Name: JianJian Li (jl4553), isi23 immanuel iclaudius
# Purpose: maze game
# Date: 11/16/2023

from maze import Maze
from room import Room


def play(my_maze: Maze):
    current = my_maze.getCurrent()
    # Play a game
    while not my_maze.atExit():
        print(current)

        direction = input("Enter direction to move north west east south restart\n")
        if direction == "north":
            if not current.getNorth():
                print("Direction invalid, try again.")
                continue
            else:
                current = current.getNorth()
                my_maze.moveNorth()
                print("You went north")
        elif direction == "west":
            if not current.getWest():
                print("Direction invalid, try again.")
                continue
            else:
                current = current.getWest()
                my_maze.moveWest()
                print("You went west")
        elif direction == "east":
            if not current.getEast():
                print("Direction invalid, try again.")
                continue
            else:
                current = current.getEast()
                my_maze.moveEast()
                print("You went east")
        elif direction == "south":
            if not current.getSouth():
                print("Direction invalid, try again.")
                continue
            else:
                current = current.getSouth()
                my_maze.moveSouth()
                print("You went south")
        elif direction == "reset":
            my_maze.reset()
            print("You went back to the start!")
            current = my_maze.getCurrent()
        else:
            print("Direction invalid, try again.")
            continue

    print("You found the exit!")


# **SIMPLE_MAZE** :  This maze should be solved when the movements east and north  are applied in that order. This
# means you arrive at the exit when you go east room and then the north room. The description of each room doesn't
# matter since the correctness will be graded. The ORDER matters. # TODO: Create the SIMPLE_MAZE
e_room = Room("This room is the entrance.")
n_room = Room("This room is the exit. Good Job.")
e_room.setNorth(n_room)
SIMPLE_MAZE = Maze(e_room, n_room)

# **INTERMEDIATE_MAZE** :  This maze should be solved when the movements are west, west, west, north, east. This
# means you arrive at the exit when you go west room, then west room again, then west room again, then take north and
# then finally the final east room. At the end of the movements, atExit should be true when it is called. The
# description of each room doesn't matter since the correctness will be graded. # TODO: Create the INTERMEDIATE_MAZE
w_room = Room("This room is the entrance.")
w_room2 = Room("west room 1")
w_room.setWest(w_room2)
w_room3 = Room("west room2")
w_room.setWest(w_room3)
w_room4 = Room("west room3")
w_room3.setWest(w_room4)
n_room2 = Room("North room")
w_room4.setNorth(n_room2)
e_room2 = Room("east room2")
n_room2.setEast(e_room2)
INTERMEDIATE_MAZE = Maze(w_room, e_room2)

if __name__ == "__main__":
    room1 = Room("This room is the entrance.")
    room2 = Room("This room has a table. Maybe a dining room?")
    room3 = Room("This room is the exit. Good Job.")
    room1.setNorth(room2)
    room2.setSouth(room1)
    room2.setEast(room3)
    room3.setWest(room2)
    myMaze = Maze(room1, room3)
    play(myMaze)
