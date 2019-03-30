from django.contrib import admin
from .models import Agenda
from .models import Agenda_Global

@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    pass

@admin.register(Agenda_Global)
class Agenda_GlobalAdmin(admin.ModelAdmin):
    pass
