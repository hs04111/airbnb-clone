from . import models
from django.views.generic import ListView
from django.shortcuts import render


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = 'rooms'


def room_detail(request, pk):
    return render(request, "rooms/detail.html")
