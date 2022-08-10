from django.shortcuts import render
from .forms import PreditctForm

def index(request):
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