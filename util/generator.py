import random


from adventure.models import Player, Room
from util.strings import name_gen, description_gen


Room.objects.all().delete()



class World:
    def __init__(self):
        self.grid = ''
        self.width = 0
        self.height = 0
    def print_rooms(self):
        '''
        Print the rooms in room_grid in ascii characters.
        '''
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
        grid = [None] * size_y
        self.width = size_x
        self.height = size_y
        for i in range(len(grid)):
            grid[i] = [None] * size_x
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
            print(x,y,room_count,can_up,can_down)
            if next_direction > 11 and can_down and not grid[y-1][x] and y > 1 and x < size_x - 2 and x > 1:
                room_direction = 'south'
                v_direction = -1
                y -= 1
            elif x > 1 and next_direction > 16 and can_up:
                room_direction = 'north'
                v_direction = 1
                y += 1
            elif h_direction > 0 and x < size_x - 1 and not grid[y][x+1]:
                room_direction = 'east'
                v_direction = 0
                x += 1
            elif h_direction < 0 and x > 0 and not grid[y][x-1]:
                room_direction = 'west'
                v_direction = 0
                x -= 1
            else:
                if grid[y+1][x]:
                    while grid[y+1][x]:
                        y += 1
                        previous_room = grid[y][x]
                y += 1
                room_direction = 'north'
                v_direction = 1
                h_direction *= -1
            room_name = name_gen()
            room_description = description_gen()
            room = Room(title=room_name, description=room_description, x=x, y=y)
            grid[y][x] = room
            room.save()
            if previous_room is not None:
                reverse_directions = {'north':'south','south':'north','east':'west','west':'east'}
                reverse_direction = reverse_directions[room_direction]
                previous_room.connectRooms(room, room_direction)
                room.connectRooms(previous_room, reverse_direction)
            if next_direction < 10 and y > 0 and grid[y-1][x]:
                room.connectRooms(grid[y-1][x], 'south')
                grid[y-1][x].connectRooms(room, 'north')
            if previous_room:
                previous_room.save()
            room.save()
            previous_room = room
            room_count += 1
        self.grid = f'{grid}'
        return


w = World()
num_rooms = 100
width = 15
height = 15
w.generate_rooms(width, height, num_rooms)
print(w.grid)

players = Player.objects.all()
for p in players:
    p.current_rooms = Room.objects.first()
    p.save()