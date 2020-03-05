from django.conf.urls import url
from . import api

urlpatterns = [
    url('init', api.initialize),
    url('move', api.move),
    url('say', api.say),
    url(r'^room/(?P<room_id>\d+)$', api.getRoomById),
    url('rooms', api.rooms)
]
