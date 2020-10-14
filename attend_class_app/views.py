from django.shortcuts import render, redirect
from .models import Units, Lesson, Class
from .forms import Uploadphoto
import joblib
from django.contrib.auth.decorators import login_required

import numpy as np
import PIL.Image
from PIL import *
from tensorflow import keras
from tensorflow.keras.models import load_model
import json
from tensorflow.keras.preprocessing.image import img_to_array
from flask import Flask, request, jsonify
import io


def attend_login(request):
    return render(request, 'attend_class_app/login.html')

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
        image = request.FILES['photo']
        print(type(image))
        pred = predictt([image])
        print(pred)
        messages.success(request,'Prediction: {}'.format(pred))

    return render(request, 'attend_class_app/upload.html')



LABELS = ["albertndege", "francisngethe",  "johnnzuki", "moseskinyua", "ronaldsamuel", "ashleywangare",  "harrysuter", "keithmartin", "patrickwainaina", "tracywanjiku", "elviswahome", "joebrian", "kennedythiga","markadalla", "geraldcastrol", "jameso", "rodneyosodo", "pricechiuri", "emmanuel", "johnnjoroge", "lynnsaidi", "richardwamalwa"]

top_model_model_path = 'themodell.h5'
top_model_weights_path = 'themodell.h5'
global model
model = load_model(top_model_model_path, compile=False)
model.load_weights(top_model_weights_path)



def prepare_image(image, target):
    # if the image mode is not RGB, convert it
    if image.mode != "RGB":
        image = image.convert("RGB")

    # resize the input image and preprocess it
    image = image.resize(target)
    image = img_to_array(image)
    image = np.array(image, dtype="float") / 255.0
    image = np.expand_dims(image, axis=0)
    # return the processed image
    return image


def predictt(image_list):
    # initialize the data dictionary that will be returned from the
    # view
    users_in_imgs = []
    # ensure an image was properly uploaded to our endpoint
    for image in image_list:
    
        # # read the image in PIL format
        image = image.open(io.BytesIO(image))

        # preprocess the image and prepare it for classificationCATEGORIES
        print(dir(image))
        image = prepare_image(image, target=(150, 150))

        # classify the input image and then initialize the list
        # of predictions to return to the client
        # data["predictions"] = []
        prediction = model.predict(x=image)[0]
        probability = np.max(prediction)
        label = LABELS[prediction.argmax()]

        users_in_imgs.append(label)

        # r = {"label": label, "probability": float(probability)}
        # data["predictions"].append(r)

        # # indicate that the request was a success
        # data["success"] = True

    # return the data dictionary as a JSON response
    return users_in_imgs