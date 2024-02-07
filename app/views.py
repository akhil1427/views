from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View,TemplateView
from app.forms import *

# Create your views here.
def fbv(request):
    return HttpResponse('<h1>This is the string from fbv')


class cbv(View):
    def get(self,request):
        return HttpResponse('cbv string')
    


def fbvhtml(request):
    return render(request,'fbv.html')

class cbvhtml(View):
    def get(self,request):
        return render(request,'cbv.html')
    

def schoolbyfbv(request):
    SFO=schoolform()
    d={'SFO':SFO}
    if request.method=='POST':
        SFDO=schoolform(request.POST)
        if SFDO.is_valid():
            SFDO.save()
            return HttpResponse('schoolbyfbv')

    return render(request,'schoolbyfbv.html',d)


class schoolbycbv(View):
    def get(self,request):
        ESF=schoolform()
        d={'ESF':ESF}
        return render(request,'schoolbycbv.html',d)
    def post(self,request):
        SF=schoolform(request.POST)
        if SF.is_valid():
            SF.save()
            return HttpResponse('schoolbycbv')

    
class cbv_template(TemplateView):
    template_name='cbv_template.html'







    
