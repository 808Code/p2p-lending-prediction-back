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
        form = PreditctForm(request.POST)
        print(form)
        context = {'form': form}
    return render(request, 'predict/index.html', context)


def index(request):
    form = PreditctForm(getRandomRecord())
    context = {'form': form}
    return render(request, 'predict/index.html', context)