from . import models
from django.views.generic import ListView
from django.urls import reverse
from django.shortcuts import render, redirect


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"


def room_detail(request, pk):
    try:
        room = models.Room.objects.get(pk=pk)
    except models.Room.DoesNotExist:
        return redirect(reverse("core:home"))
    return render(request, "rooms/detail.html", {"room": room})
