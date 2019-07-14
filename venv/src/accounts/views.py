from django.shortcuts import render
from django.contrib.auth.froms import UserCreationFrom
# Create your views here.

def signup_view(request):
    from = UserCreationFrom(),
    return render(request,'accounts/signup.html', {'from':from})
