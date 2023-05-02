from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import SignupForm
# Create your views here.


def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

