from django.shortcuts import render
from django.http import HttpResponse
from .models import Image
# Create your views here.
def home(request):
    img = Image.objects.all()
    return render(request=request, template_name='index.html', context={'image': img})
    