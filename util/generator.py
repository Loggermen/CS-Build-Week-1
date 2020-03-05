from adventure.models import Player, Room
from util.strings import name_gen, description_gen
import random


class World:
    def __init__(self):
        self.grid = None
        self.width = 0
        self.height = 0

    def print_rooms(self):
        """
        Print the rooms in room_grid in ascii characters.
        """
        # Add top border
        str = "# " * ((3 + self.width * 5) // 2) + "\n"
        # The console prints top to bottom but our array is arranged
        # bottom to top.
        #
        # We reverse it so it draws in the right direction.
        reverse_grid = list(self.grid) # make a copy of the list
        reverse_grid.reverse()
        for row in reverse_grid:
            # PRINT NORTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.n_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
            # PRINT ROOM ROW
            str += "#"
            for room in row:
                if room is not None and room.w_to is not None:
                    str += "-"
                else:
                    str += " "
                if room is not None:
                    str += f"{room.id}".zfill(3)
                else:
                    str += "   "
                if room is not None and room.e_to is not None:
                    str += "-"
                else:
                    str += " "
            str += "#\n"
            # PRINT SOUTH CONNECTION ROW
            str += "#"
            for room in row:
                if room is not None and room.s_to is not None:
                    str += "  |  "
                else:
                    str += "     "
            str += "#\n"
        # Add bottom border
        str += "# " * ((3 + self.width * 5) // 2) + "\n"
        # Print string
        print(str)

    def generate_rooms(self, size_x, size_y, num_rooms):
        self.grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(self.grid)):
            self.grid[i] = [None] * size_x
        x = -1
        y = 0
        room_count = 0
        h_direction = 1
        v_direction = 1
        previous_room = None
        while room_count < num_rooms:
            next_direction = random.randint(0,18)
            can_down = v_direction <= 0
            can_up = v_direction >= 0
            if next_direction > 11 and can_down and not self.grid[y - 1][x] and y > 1 and size_x - 2 > x > 1:
                room_direction = 's'
                v_direction = -1
                y -= 1
            elif x > 1 and next_direction > 16 and can_up:
                room_direction = 'n'
                v_direction = 1
                y += 1
            elif h_direction > 0 and x < size_x - 1 and not self.grid[y][x+1]:
                room_direction = 'e'
                v_direction = 0
                x += 1
            elif h_direction < 0 and x > 0 and not self.grid[y][x-1]:
                room_direction = 'w'
                v_direction = 0
                x -= 1
            else:
                if self.grid[y+1][x]:
                    while self.grid[y+1][x]:
                        y += 1
                        previous_room = self.grid[y][x]
                y += 1
                room_direction = 'n'
                v_direction = 1
                h_direction *= -1
            room_name = name_gen()
            room_description = description_gen()
            room = Room(title=room_name, description=room_description, x=x, y=y)
            self.grid[y][x] = room
            room.save()
            if previous_room is not None:
                reverse_directions = {'n':'s','s':'n','e':'w','w':'e'}
                reverse_direction = reverse_directions[room_direction]
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_direction)
            if next_direction < 10 and y > 0 and self.grid[y-1][x]:
                room.connectRooms(self.grid[y-1][x], 's')
                self.grid[y-1][x].connectRooms(room, 'n')
            if previous_room:
                previous_room.save()
            room.save()
            previous_room = room
            room_count += 1
