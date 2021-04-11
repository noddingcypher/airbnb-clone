from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.RoomType)
class ItermAdmin(admin.ModelAdmin):
    pass


@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    """ Room Model Definition """

    pass
