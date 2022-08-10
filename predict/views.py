from django.shortcuts import render
from .forms import PreditctForm
import pickle

filename = 'LendingClubPredictingModel.sav'
ML_MODEL = pickle.load(open(filename, 'rb'))

def index(request):
    print(ML_MODEL)
    if request.method == 'POST':
        form = PreditctForm(request.POST)
        if form.is_valid():
            print(form)
            context = {'form': form}
            return render(request, 'predict/index.html', context)
    else:
        form = PreditctForm()
        context = {'form': form}
    return render(request, 'predict/index.html', context)