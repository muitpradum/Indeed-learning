from django.urls import path
from . import views
urlpatterns=[
    path('index/', views.index),
    path('',views.index),
    path('contact/',views.contact),
    path('home/',views.home),
    path('about/',views.aboutus),
    path('batches/',views.batches),
    path('registration/',views.registration),
    path('facility/',views.facility),
    path('placement/',views.ourplacement),
    path('login/',views.login),
    path('feedback/',views.feedback),
]