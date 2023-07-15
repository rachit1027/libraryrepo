from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True) # ek additional field add ki hai apan ne 
    first_name = forms.CharField()
    last_name = forms.CharField()
	
    class Meta:
      model = User # pehle se hi bana rehta hai iska models
      fields = ("username",'first_name','last_name', "email", "password1", "password2")

	# def save(self, commit=True):
	# 	user = super(NewUserForm, self).save(commit=False)
	# 	user.email = self.cleaned_data['email']
	# 	if commit:
	# 		user.save()
	# 	return user