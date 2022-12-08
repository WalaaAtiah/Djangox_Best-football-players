from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Player


class PlayerListView(ListView):
    template_name = "pages/home.html"
    model = Player


class PlayerDetailView(DetailView):
    template_name = "pages/player-detail.html"
    model = Player


class PlayerCreateView(CreateView):
    template_name = "pages/create.html"
    model = Player
    fields = ["name","team","position","Age","publisher","data","image"]


class PlayerUpdateView(UpdateView):
    template_name = "pages/player-update.html"
    model = Player
    fields = []


class PlayerDeleteView(DeleteView):
    template_name = "pages/player-delete.html"
    model = Player
    success_url = reverse_lazy("player_list")