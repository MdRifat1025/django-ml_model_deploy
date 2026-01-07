from django.shortcuts import render
import numpy as np
import joblib
from django.conf import settings
import os

MODEL_PATH = os.path.join(settings.BASE_DIR, 'predictor', 'model', 'iris_model.pkl')
model=joblib.load('predictor/model/iris_model.pkl')
def predict_view(request):
    prediction=None
    if request.method == 'POST':
        f1=request.POST['f1']
        f2=request.POST['f2']   
        f3=request.POST['f3']
        f4=request.POST['f4']
        
        data=np.array([[f1,f2,f3,f4]],dtype=float)
        prediction=model.predict(data)[0]



    return render(request,'predictor/predict.html',{'prediction':prediction})