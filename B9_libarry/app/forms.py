
# import the standard Django Forms
# from built-in library
from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User,Group

	
# creating a form
class InputForm(forms.Form):
	
	first_name = forms.CharField(max_length = 200)
	last_name = forms.CharField(max_length = 200)
	roll_number = forms.IntegerField(
					help_text = "Enter 6 digit roll number" #matlab ye pehle se likha rahega
					)
	password = forms.CharField(widget = forms.PasswordInput())
# ------------------------------------------------------------------------------------------------------------------------------------------------------

# - Dheko upar wala form apan ne banaya hai 
# ab neeche jo form hai jo models me feilds hai uspe banega

class BookForm(forms.ModelForm):
	# jaise agar koi nayi feild chaiye apan ko to apan idhar likh saktey hai 
	class Meta:
		model = Book
		fields = "__all__" # mujhe saarey feilds chaiye
exclude = ("is_active",) # ue mujhe nahi chaiye

# ------------------------------------------------------------------------------------------------------------------------
STATES = (
    ('', 'Choose...'),
    ('MG', 'Minas Gerais'),
    ('SP', 'Sao Paulo'),
    ('RJ', 'Rio de Janeiro')
)

class AddressForm(forms.Form):
    email = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
    password = forms.CharField(widget=forms.PasswordInput())
    address_1 = forms.CharField(
        label='Address',
        widget=forms.TextInput(attrs={'placeholder': '1234 Main St'})
    )
    address_2 = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Apartment, studio, or floor'})
    )
    city = forms.CharField()
    state = forms.ChoiceField(choices=STATES)
    zip_code = forms.CharField(label='Zip')
    check_me_out = forms.BooleanField(required=False)

# -------------------------------------------------------------------------------------------------------------------------------------------

