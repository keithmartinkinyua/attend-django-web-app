from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Units

context = {
            'units': Units.objects.all()
        }


def home(request):

    context = {
        'units': Units.objects.all()
    }
    return render(request, 'attend_class_app/home.html', context)



class UnitListView(ListView):
    model = Units
    template_name = 'attend_class_app/home.html'
    context_object_name = 'units'

#class UnitDetailView(DetailView):
    #model = Units
    #template_name = 'attend_class_app/unit_detail.html'
    #context_object_name = 'units'
    

def UnitDetailView(request):
    #if request.method == 'POST':
        #print(context)
    return render (request, 'attend_class_app/unit_detail.html' , { 'context' : context })

def about(request):
    return render(request, 'attend_class_app/about.html', {'title':'About'})  