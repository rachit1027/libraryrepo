from django.shortcuts import render,HttpResponse
from .forms import NewUserForm
# Create your views here.
def user_signup(request):
    if request.method == 'POST':
        form = NewUserForm() # form ke pass new user form aa gaya hai
        if form.is_valid(): # valid hai ki nahi check kar rahe hai
            form.save() # auth user table me ab iski entry hogi
            return HttpResponse
    elif request.method == "GET":
        form = NewUserForm()
        return render(request=request,template_name="register.html",context={"signup_form":form})
    
# how register is working
#1. urls me jaaega fir views me 
#2. views me aa ke "get" method me jaaega
#3. and jo humne variable assign kitya hai form ke naam se usme apan ne apna NEwUserForm de diya hai
#4. views usko register.html fetch karney ko bolega 
#5. and humne register.html me context pass kar diya as as dictionary "context={"register_form":form}"