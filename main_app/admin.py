from django.contrib import admin
from .models import Trips, Destinations, Photos, Checklist, Activities, TripRequest

# Register your models here.
admin.site.register(Trips)
admin.site.register(Destinations)
admin.site.register(Photos)
admin.site.register(Checklist)
admin.site.register(Activities)
admin.site.register(TripRequest)
