from django.shortcuts import render
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
import csv,io 
from django.contrib.auth.models import User, auth
from .models import Prediction
from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def heart(request):
    
    dict1 = request.POST
    with open('csv1.csv','w') as csvfile:
        wrt = csv.writer(csvfile)
        for key, value in dict1.items():
                wrt.writerow([key,value])

    
    
   
    df = pd.read_csv('static/Heart_train.csv') #Reading the training data set.
    data = df.values
    X = data[:, :-1]
    Y = data[:, -1:]


    value = ''

    if request.method == 'POST':    #Storing the data given by user

        age = float(request.POST['age'])
        name = request.POST['name']
        sex = float(request.POST['sex'])
        cp = float(request.POST['cp'])
        trestbps = float(request.POST['trestbps'])
        chol = float(request.POST['chol'])
        fbs = float(request.POST['fbs'])
        restecg = float(request.POST['restecg'])
        thalach = float(request.POST['thalach'])
        exang = float(request.POST['exang'])
        oldpeak = float(request.POST['oldpeak'])
        slope = float(request.POST['slope'])
        ca = float(request.POST['ca'])
        thal = float(request.POST['thal'])
        
         #Storing the Data in Array
        '''
        reshape: Gives a new shape to an array without changing its data.
        '''      


        user_data = np.array(
            (age,
             sex,
             cp,
             trestbps,
             chol,
             fbs,
             restecg,
             thalach,
             exang,
             oldpeak,
             slope,
             ca,
             thal)
        ).reshape(1, 13)

        
         '''
        Working of Random Forest Classifier :
        1. Select Random Samples from DataSet
        2. Construct a decision tree for each sample and get a prediction result from each decision tr
        3. Perform a vote for each predicted result.
        4. Select the prediction result with the most votes as the final prediction.
        for more visit : https://www.datacamp.com/community/tutorials/random-forests-classifier-python
        '''
            
        rf = RandomForestClassifier(
            n_estimators=16,
            criterion='entropy',
            max_depth=9
        )

        rf.fit(np.nan_to_num(X), Y)
        rf.score(np.nan_to_num(X), Y)
        predictions = rf.predict(user_data)  #passing the data and storing the result


        if int(predictions[0]) == 1:
            value = 'HAVE'
        elif int(predictions[0]) == 0:
            value = "DON\'T "

        prediction = Prediction(pname=name, page=age, pgender=sex, pcp=cp, ptrestbps=trestbps, pchol=chol, pfbs=fbs, prestecg=restecg, pthalach=thalach, pexang=exang, poldpeak=oldpeak, pslope=slope, pca=ca, pthal=thal, presult=value
        )
        prediction.save()

        heart_value_dict={"name":name,"age":age,"sex":sex,"cp":cp,"trestbps":trestbps,"chol":chol,"fbs":fbs,"restecg":restecg,"thalach":thalach,"exang":exang,"oldpeak":oldpeak,"slope":slope,"ca":ca,"thal":thal,"result":value}
        print(heart_value_dict)
    return render(request,'heart.html',{'context': value})



def home(request):

    return render(request,'home.html')

""" 
Handling 404 error pages. 
"""
def handler404(request):
    return render(request, '404.html', status=404)



    
