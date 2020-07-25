from django.shortcuts import render
from django.views.generic import (ListView, DetailView, View)
from .models import Units
from django import template

register = template.Library()


arr = []
context =  Units.objects.all().values()

for i in context:
    arr.append(i)

print(arr)


def home(request):
    return render(request, 'attend_class_app/home.html', context)

# class UnitListView(ListView):
#     print(context)
#     model = Units
#     template_name = 'attend_class_app/home.html'
#     context_object_name = 'units'

def UnitListView(request):
    units =  Units.objects.all()
    return render(request, "attend_class_app/home.html", {"units": units})



# def UnitDetailView(request):
#     print(context)
#     units =  Units.objects.all()

#     return render(request, "attend_class_app/home.html", {"units": units})



class UnitDetailView(View):
    def get(self, request, *args, **kwargs):
        # id  = request.GET["id"]
        return render(request, 'attend_class_app/unit_detail.html', {'units' :arr})

 
    

# def UnitDetailView(request):
#     if request.method == 'POST':
#         print(context)
#     return render (request, 'attend_class_app/unit_detail.html' , { 'context' : context })

def about(request):
    return render(request, 'attend_class_app/about.html', {'title':'About'})  