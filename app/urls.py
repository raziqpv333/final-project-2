from django.urls import path
from . import views

urlpatterns=[
    path('main',views.main),
    path('',views.login),
    path('register/',views.registration),
    path('contact/', views.contact_view, name='contact'),  
    path('logout/', views.logout),
]