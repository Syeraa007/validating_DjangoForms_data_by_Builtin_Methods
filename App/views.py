from django.shortcuts import render
from django.http import HttpResponse
from App.forms import *
from App.models import *
# Create your views here.
def sform(request):
    SFO=Student()
    d={'SFO':SFO}
    if request.method=='POST':
        SDF=Student(request.POST)
        if SDF.is_valid():
            print(str(SDF.cleaned_data))
            StudentForm.objects.get_or_create(name=SDF.cleaned_data['name'],age=SDF.cleaned_data['age'],loc=SDF.cleaned_data['loc'],email=SDF.cleaned_data['email'],remail=SDF.cleaned_data['remail'],url=SDF.cleaned_data['url'],phone=SDF.cleaned_data['phone'])
            return HttpResponse('Data submitted')
        else:
            return HttpResponse('Invalid Data')
    return render(request,'sform.html',d)

def show_sform(request):
    SAD=StudentForm.objects.all()
    d={'SAD':SAD}
    return render(request,'show_sform.html',d)