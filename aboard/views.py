from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse 
from django.template import loader
from .models import Ch
from .models import ActCard
from .models import SituationEvent
import random
from time import time
from django.http import JsonResponse

# Create your views here.
class AjaxHandlerView(View):
    def get(self, request):
        number_of_records = SituationEvent.objects.count()
        
        #Катастрофа
        random_index = int(random.random()*number_of_records)+1
        e1 = SituationEvent.objects.get(pk=random_index)
        # О бункере
        random_index = int(random.random()*number_of_records)+1
        e2 = SituationEvent.objects.get(pk=random_index)

        random_index = int(random.random()*number_of_records)+1
        e3 = SituationEvent.objects.get(pk=random_index)

        random_index = int(random.random()*number_of_records)+1
        e4 = SituationEvent.objects.get(pk=random_index)

        # Еда
        random_index = int(random.random()*number_of_records)+1
        e5 = SituationEvent.objects.get(pk=random_index)

        # В бункере
        random_index = int(random.random()*number_of_records)+1
        e6 = SituationEvent.objects.get(pk=random_index)
        random_index = int(random.random()*number_of_records)+1
        e7 = SituationEvent.objects.get(pk=random_index)
        random_index = int(random.random()*number_of_records)+1
        e8 = SituationEvent.objects.get(pk=random_index)
        eve = [e1.event, e2.aboutb, e3.aboutb, e4.aboutb, e5.timer, e6.containb,e7.containb,e8.containb]

        if request.is_ajax():
            number_of_records = Ch.objects.count()

            random_index = int(random.random()*number_of_records)+1
            b1 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b2 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b3 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b4 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b5 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b6 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b7 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b8 = Ch.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            b9 = Ch.objects.get(pk=random_index)

            number_of_records = ActCard.objects.count()

            random_index = int(random.random()*number_of_records)+1
            k1 = ActCard.objects.get(pk=random_index)

            random_index = int(random.random()*number_of_records)+1
            k2 = ActCard.objects.get(pk=random_index)
            
            info = [b1.gender, b9.age, b2.profession, b3.health, b4.shape, b5.hobby, b6.fobies, b7.inventory, b8.info, k1.act, k2.act]

            return JsonResponse({'seconds': info, 'eve':eve}, status=200)
        return render(request, 'aboard/index.html', {'eve':eve})

