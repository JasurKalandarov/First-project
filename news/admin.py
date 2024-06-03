from django.contrib import admin
from news.models import Event, EventVillian, Hero
# Register your models here.

admin.site.register([Event, EventVillian, Hero])
