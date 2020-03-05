from django.contrib.auth.models import User
from adventure.models import Player, Room
from util.strings import name_gen, description_gen
from util.generator import World
import random

Room.objects.all().delete()

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

# DEBUGGING:
# w.print_rooms()
for room in Room.objects.all():
    print(f"\
    id: {room.id}\n\
    title: {room.title}\n\
    description: {room.description}\n\
    n_to: {room.n_to}\n\
    s_to: {room.s_to}\n\
    e_to: {room.e_to}\n\
    w_to: {room.w_to}\n\
    x: {room.x}\n\
    y: {room.y}\n\n")
