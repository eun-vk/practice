from django.urls import path
from . import views

urlpatterns = [
    # /chat/
    path("", views.index),

    # /chat/messages/new/
    path("messages/new/", views.chat_message_new),

    # /chat/puzzle/name/
    path("puzzle/<str:name>/", views.puzzle_room),
]