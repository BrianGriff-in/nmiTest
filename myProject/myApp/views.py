from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Image, ImageQRCode, ImageIcons
# Create your views here.
def home(request):
    img = Image.objects.all()
    img1 = ImageQRCode.objects.all()
    return render(request=request, template_name='myApp/index.html', context={'image': img, 'qrImages': img1})

def detail(request, id):
    icons = get_object_or_404(ImageIcons, id=id)
    return render(request=request, template_name='myApp/index.html', context={'imgIcons': icons})