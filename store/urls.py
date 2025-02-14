from django.urls import path
from . import views

urlpatterns =[
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('login/',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
    path('register/',views.register_user,name='register'),
    path('product/<int:pk>',views.product,name='product'), # pk is only a variable
    path('category/<str:foo>',views.category,name='category'), # foo is only a variable
]