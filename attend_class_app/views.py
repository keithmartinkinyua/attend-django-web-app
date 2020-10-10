from django.shortcuts import render
from django.views.generic import (ListView, DetailView, View)
from .models import Units
from .forms import Uploadphoto
import joblib




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



def themodel(request):
    mdl=joblib.load("my_4.2_model_weights.pkl")
    face =request.data
    pred = mdl.predict(face)
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


def facesystem(request):

    if request.method == "POST":
        form = Uploadphoto(request.POST)
        if form.is_valid():
            image = form.cleaned_data['image']
            pred = themodel(image)
            messages.success(request,'Prediction: {}'.format(pred))
    
    form = Uploadphoto()

    return render( request, 'attend_class_app/upload.html', {'form':form})