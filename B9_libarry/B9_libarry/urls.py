"""
URL configuration for B9_libarry project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app.views import welcome_page,show_books,show_single_book,add_single_book,edit_single_book,delete_single_book,soft_delete_single_book,form_view
from user_app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path("book/home/",welcome_page,name="home_page"),
    path("book/show_books/",show_books,name="show_books"),
    path("book/show_single_book/<int:bid>/", show_single_book, name="show_single_book"),
    path("book/add_book/", add_single_book, name="add_single_book"),
    path('book/edit_single_book/<int:bid>/',edit_single_book,name="edit_single_book"),
    path('book/delete_book/<int:bid>/',delete_single_book,name="delete_single_book"),
    path('book/soft_delete_book/<int:bid>/',soft_delete_single_book,name="soft_delete_single_book"),
    path('book/form_view',form_view,name="form_view"),
           #idhar apan ne book iskiye likha ki confusion na ho ki book ka hai ya user ka 
    #user app urls
    path("user/signup/",views.user_signup,name="user_signup")
]

# patterns/urls/endpoints
# http://127.0.0.1:8000/book/admin/
# http://127.0.0.1:8000/book/home/
# http://127.0.0.1:8000/book/show_books
# http://127.0.0.1:8000/book/show_single_book/1/
# http://127.0.0.1:8000/book/add_book
# http://127.0.0.1:8000/book/edit_single_book/1
# http://127.0.0.1:8000/book/delete_book/1
# http://127.0.0.1:8000/book/soft_delete_book/1
# http://127.0.0.1:8000/book/form_view

# user_app urls
#http://127.0.0.1:8000/user/user_registration