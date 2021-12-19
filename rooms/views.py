from django.views.generic import ListView, DetailView
from django.shortcuts import render
from django_countries import countries
from . import models

# Create your views here.


class HomeView(ListView):

    """HomeView Definition"""

    model = models.Room
    paginate_by = 10
    ordering = "created"
    paginate_orphans = 6
    context_object_name = "rooms"


class RoomDetail(DetailView):

    """ RoomDetail Definition """

    model = models.Room
    pk_url_kwarg = "pk"


def search(request):
    city = request.GET.get("city", "Anywhere")
    city = str.capitalize(city)
    country = request.GET.get("country", "KR")
    room_type = int(request.GET.get("room_type", 0))
    room_types = models.RoomType.objects.all()

    form = {
        "city": city,
        "selected_country": country,
        "selected_room_type": room_type,
    }

    choices = {
        "room_types": room_types,
        "countries": countries,
    }
    return render(
        request,
        "rooms/search.html",
        {**form, **choices},
    )
