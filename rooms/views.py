from django.views.generic import ListView, DetailView
from django.shortcuts import render
from . import models


class HomeView(ListView):

    """ HomeView Definition """

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 5
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room


# from django.http import Http404
# from django.urls import reverse
# from django.shortcuts import render  , redirect

# def room_detail(request, pk):
#     try:
#         room = models.Room.objects.get(pk=pk)
#         return render(request, "rooms/detail.html", {"room": room})
#     except models.Room.DoesNotExist:
#         raise Http404()
#         # return redirect(reverse("core:home"))
#         # 방 pk가 모델에 없는 경우 redirect로 home으로 보낼 수도 있고, 아니면 404 에러를 일으킬 수 있다.
#         # Http404를 일으키는 경우, 만약 templates 폴더에 404.html이 있으면 debug=True일 경우 이 html이 render된다.


def search(request):
    city = request.GET.get("city")
    city = str.capitalize(city)
    return render(request, "rooms/search.html", {"city": city})