from django.shortcuts import render
from django.views.generic import ListView
from .models import Agenda
from .models import Agenda_Global

class HomePageView(ListView):
    model = Agenda
    template_name = 'app_agenda/home.html'

