from django.shortcuts import render
from .models import Media
def medai_list(request):
    media_objects =Media.objects.all()
    return render(request, 'list.html', {'media_objects': media_objects})