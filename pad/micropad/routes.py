from django.shortcuts import render
from boogie.router import Router
from django.shortcuts import redirect
urlpatterns = Router()

@urlpatterns.route('')
def home(request):
    ctx={}
    print("Home")
    return render(request, 'home.html',ctx)

