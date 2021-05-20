from django.shortcuts import render
from .models import Radio
from django.views.generic import ListView


class RadioListView(ListView):
    model = Radio
    template_name = 'radio/radio_index.html'
    context_object_name = 'podcasts'


def podcast(request):
    podcasts = Radio.objects.all()
    return render(request, 'radio/radio_index.html',
                  {'podcasts': podcasts})
