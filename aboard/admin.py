from django.contrib import admin

# Register your models here.
from .models import Ch
from .models import ActCard
from .models import SituationEvent
admin.site.register(Ch)
admin.site.register(ActCard)
admin.site.register(SituationEvent)