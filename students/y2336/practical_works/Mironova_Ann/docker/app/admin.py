from django.contrib import admin
from .models import *


admin.site.register(flight_information)
admin.site.register(helicopter)
admin.site.register(crew_member)
admin.site.register(flight)
admin.site.register(helicopter_crew_identification)

# Register your models here.
