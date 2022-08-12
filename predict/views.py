from django.shortcuts import render
from .forms import PreditctForm
import pickle
from .service import getRandomRecord
filename = 'LendingClubPredictingModel.sav'
ML_MODEL = pickle.load(open(filename, 'rb'))

def check(request):
    context={}
    if request.method == 'POST':
        d=request.POST.dict()
        del d['csrfmiddlewaretoken']
        test_values=list(d.values())
        prediction=ML_MODEL.predict([test_values])
        form = PreditctForm(initial=d)
        context['form'] = form
        boolean_prediction=1 if prediction==1 else 2
        context['boolean_prediction']=boolean_prediction
    return render(request, 'predict/index.html', context)


def index(request):
    context={}
    form = PreditctForm(getRandomRecord())
    context['boolean_prediction'] = 3
    context['form'] = form
    return render(request, 'predict/index.html', context)