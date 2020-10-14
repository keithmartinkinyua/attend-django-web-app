from django.shortcuts import render, redirect
from django.views.generic import (ListView, DetailView, View)
from .models import Units, Lesson, Class
from .forms import Uploadphoto
import joblib
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, 'attend_class_app/home.html', context)

@login_required
def UnitListView(request):
    if request.user.is_superuser:
        return redirect('attend-units')
    # classes =  Class.objects.filter(user = request.user)
    # for a_class in classes:
    #     print(a_class.units)

    units = Units.objects.all()
    return render(request, "attend_class_app/home.html", {"units": units})



# def UnitDetailView(request):
#     print(context)
#     units =  Units.objects.all()

#     return render(request, "attend_class_app/home.html", {"units": units})


@login_required
def unit(request, id):
    unit = Units.objects.get(id = id)
    print(unit)
    return render(request, 'attend_class_app/unit_detail.html', {'unit' :unit})

 
def about(request):
    return render(request, 'attend_class_app/about.html', {'title':'About'})  



def themodel(image):
    mdl=joblib.load("my_4.2_model_weights.pkl")
    pred = mdl.predict(image)
    return pred


## the form data
'''def cxcontact(request):
	if request.method=='POST':
		form=ApprovalForm(request.POST)
		if form.is_valid():
				Firstname = form.cleaned_data['firstname']
				Property_Area = form.cleaned_data['Property_Area']
				myDict = (request.POST).dict()
				df=pd.DataFrame(myDict, index=[0])
				answer=approvereject(ohevalue(df))[0]
				Xscalers=approvereject(ohevalue(df))[1]
				print(Xscalers)
				messages.success(request,'Application Status: {}'.format(answer))
	
	form=ApprovalForm()
				
	return render(request, 'myform/cxform.html', {'form':form})'''

@login_required
def units_admin(request, id):
    if not request.user.is_superuser:
        return redirect('attend-home')
   
    lessons = Lesson.objects.filter(unit= id)
    unit = Units.objects.get(id = id)
    print(lessons)
    return render( request, 'attend_class_app/lessons.html', {'lessons':lessons, 'unit':unit })


def all_units(request):
    if not request.user.is_superuser:
        return redirectr('attend-home')
    
    units = Units.objects.all()

    return render(request, 'attend_class_app/units.html', {'units': units})

def records(request, id):
    if not request.user.is_superuser:
        return redirect('attend-home')

    lesson = Lesson.objects.get(id = id)
     
    if request.method == "POST":
        
        image = form.cleaned_data['image']
        print(type(image))
        pred = themodel(image)
        print(pred)
        messages.success(request,'Prediction: {}'.format(pred))

    return render(request, 'attend_class_app/upload.html')

