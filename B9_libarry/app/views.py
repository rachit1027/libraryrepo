from django.shortcuts import render,HttpResponse,redirect
from .models import Book
import datetime

# Create your views here.

#FBB - Function based view
def welcome_page(request):
    return render(request,"welcome.html")

def show_books(request):
    books = Book.objects.filter(is_active=True)
    return render(request,"show_books.html", {"allbooks":books, "today":datetime.datetime.now() })

def show_single_book(request, bid): # ye apan ne iske url me int diya hai uska naam ID hai
    try:
        book_obj =  Book.objects.get(id = bid)
    except Book.DoesNotExist:
           return HttpResponse("Book does not exist")
    return render(request=request, template_name="bookdetail.html", context={"book" :book_obj})
                   # apan keyword argument pass kar rahe hai isliye hamesha usko context bol ke hi pass karna
    
def add_single_book(request):
     if request.method == "POST":
          final_dict = request.POST 
        #   print(final_dict) #'nm': ['book4'], 'prc': ['454'], 'qty': ['80'], 'is_pub': ['Yes']}> # apan neadd book waale html me radio button ko value de di yes and No
          book_name, book_price, book_qty, book_is_pub = common_var()
          if book_is_pub == "Yes":
               is_pub = True
          else:
               is_pub = False
          Book.objects.create(name=book_name,price = book_price,qty = book_qty,is_published=is_pub)
          return redirect("show_books")
        # print(request.POST) #name me apan ne jo "nm" de rakha hai addbook.html me vo yaha pe kaam aa raha hai
     elif request.method == "GET":
         return render (request, "addbook.html")
# add_single_book ka funda
# pehle GET request jaaegi form aa jaaega
# form jaise hi submit karoge fir idhar aaega and fir POST request jaaegi

def common_var(request):
     final_dict = request.POST 
     book_name = final_dict.get("nm")
     book_price = final_dict.get("prc")
     book_qty = final_dict.get("qty")
     book_is_pub = final_dict.get("ispub") 
     return book_name,book_price,book_qty,book_is_pub

def edit_single_book(request,bid):
     book_obj = Book.objects.get(id=bid) # ye dono ko lag raha hai isliye idhar rakha hai
     if request.method == "GET":
        return render(request,"bookedit.html",{"single_book":book_obj})
     elif request.method == "POST":
          book_name, book_price, book_qty, book_is_pub = common_var()
          if book_is_pub == "Yes":
               is_pub = True
          else:
               is_pub = False

# JO data aa raha hai uska naam ye update kar ke rakho neeche ye kar rahe hai
          book_obj.name = book_name
          book_obj.price = book_price
          book_obj.qty = book_qty
          book_obj.is_published = is_pub
          book_obj.save()
          return redirect("show_books")
          
        #   print("in post request")


def delete_single_book(request,bid):
     book_obj = Book.objects.get(id=bid)
     book_obj.delete()
     return redirect("show_books")

def soft_delete_single_book(request,bid): #soft delete
     book_obj = Book.objects.get(id=bid)
     book_obj.is_active = False
     book_obj.save()
     return redirect("show_books")

# ------------------------------ FOR DJANGO FORMS ---------------------------------------------------

# from django.shortcuts import render
from .forms import InputForm,BookForm,AddressForm
  
# Create your views here.
def form_view(request):
   if request.method == "POST":
        print("in post")
        data = request.POST # backend me data aa raha hai 
        form = BookForm(data)# book form jo banaya hai apan ne usko data diya jo bhi book apan add karenge 
        if form.is_valid():
             form.save() # database me save karo
        return redirect("show_books")
#     print(InputForm())
   elif request.method == "GET":
      print("in get request")
      return render(request, "bookformtest.html", {"bookform":BookForm()}) # ek dictionary create ki jisme key "form " hai and valur Inputform  hai or apan ab isko kahi bhi call kar saktey hai ]



# <!-- <form method="post">
#     {% csrf_token %}
#     <div class="form-row">
#       <div class="form-group col-md-6 mb-0">
#         {{ form.email|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-6 mb-0">
#         {{ form.password|as_crispy_field }}
#       </div>
#     </div>
#     {{ form.address_1|as_crispy_field }}
#     {{ form.address_2|as_crispy_field }}
#     <div class="form-row">
#       <div class="form-group col-md-6 mb-0">
#         {{ form.city|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-4 mb-0">
#         {{ form.state|as_crispy_field }}
#       </div>
#       <div class="form-group col-md-2 mb-0">
#         {{ form.zip_code|as_crispy_field }}
#       </div>
#     </div>
#     {{ form.check_me_out|as_crispy_field }}
#     <button type="submit" class="btn btn-primary">Sign in</button>
#   </form> -->

# yess sir new virew added