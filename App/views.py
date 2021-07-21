from django.shortcuts import render
from .models import Testdata
# Create your views here.
def home(request):
    db=Testdata.objects.all()
    return render(request, 'home.html', {'data':db})
