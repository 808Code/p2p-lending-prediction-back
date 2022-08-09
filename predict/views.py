from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from loanprediction.predict.forms import PreditctForm


def index(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = PreditctForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'name.html', {'form': form})
    return render(request, 'predict/index.html', context)