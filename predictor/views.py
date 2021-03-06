from django.shortcuts import render
from django.template import loader
import pandas as pd
from django.http import HttpResponse
import numpy as np
import pickle
from sklearn import tree

from sklearn.model_selection import train_test_split
from sklearn.metrics import make_scorer, accuracy_score
from sklearn.model_selection import GridSearchCV

from sklearn import metrics
from pandas._libs.parsers import na_values
from pandas.tests.io.parser import skiprows
from sklearn import neighbors, preprocessing, cross_validation

from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, render_to_response
from django.db.models import Q
from django.views.decorators.csrf import csrf_protect, ensure_csrf_cookie
from django.template import Context
from django.template.loader import get_template
from django.http import HttpResponseNotFound, HttpResponseServerError

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from predictor.models import Person


# Create your views here

def index(request):
    return render(request, 'predictor/index.html')

def about(request):
    return render(request, 'predictor/about.html')

def home(request):
    return render(request, 'predictor/home.html')


def pastdata(request):
    return render(request, 'predictor/pastdata.html')


def add_data(request):
    return render(request, 'predictor/adddata.html')


def login_users(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                c = {}
                return render(request, 'predictor/home.html', c)
            else:
                return render(request, 'predictor/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'predictor/login.html', {'error_message': 'Invalid login'})
    return render(request, 'predictor/login.html')


def register(request):
    # if request.method == "POST":
    #     username = request.POST['username']
    #     password = request.POST['password']
    #     user = authenticate(username=username, password=password)
    #     login(request, user)
    #     return render(request, 'predictor/home.html', {'error_message': 'Sucessfully Registered'})
    # else:
    #     return render(request, 'predictor/register.html', {'error_message': 'Registration Unsuccessfull'})
    return render(request, 'predictor/register.html')


def predictorform(request):

    return render(request, 'predictor/form.html')

def spillpredictor(request):

    year = request.POST.get('year')
    month = request.POST.get('month')
    date = request.POST.get('date')
    storage = request.POST.get('storage')
    outlet = request.POST.get('outlet')
    inflow = request.POST.get('inflow')
    rainfall = request.POST.get('rainfall')

    userInputs = [year, month, date, storage, outlet, inflow, rainfall]

    if year is None:
        print("its null")
    else:
        userInputsFormatted = list(map(float, userInputs))

        dataset = pd.read_csv('C:/Users/Chanaka Rathnakumara/Desktop/Test/FinalFormattedData.csv', na_values="?")

        dataset.dropna(inplace=True, axis=0, how="any")

        dataset.apply(pd.to_numeric)

        X = dataset.loc[:, "Year":"Rainfall"]

        y = dataset["Elevation"]

        # print('print X_test', X)
        # print('print X_test', y)

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3)

        # print('print X_test', X_test)
        # print('print', X_train)

        clf = tree.DecisionTreeClassifier()
        clf.fit(X_train, y_train)

        accuracy1 = []
        predictions = clf.predict(X_test)
        y_pred = clf.predict(X_test)
        print("printing chances: ", y_pred[:10])
        accuracy = float(accuracy_score(y_test, predictions))
        accuracy1.append(accuracy)
        print("acuracy score is ",accuracy1 )
        prediction = clf.predict([userInputsFormatted])

        print('prediction is ', prediction)
        loader.get_template('predictor/form.html')
        template=loader.get_template('predictor/prediction.html')
        context = {
         'allUsers': prediction,
         'accuracy': accuracy1,
         }

        return HttpResponse(template.render(context,request))
    template = loader.get_template('predictor/form.html')

    context = {

    }
    return HttpResponse(template.render(context, request))
