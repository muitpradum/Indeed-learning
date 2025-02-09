from django.urls import path
from . import views
urlpatterns=[
    path('index/',views.index),
    path('',views.index),
    path('batches/',views.batches),
    path('lecture/',views.lecture),
    path('notes/',views.notes),
    path('logout/',views.logout),
    path('tasks/',views.tasks),
    path('swkit/',views.swkit),
    path('liveclasses/',views.liveclasses),
    path('uprofile/',views.uprofile),
    path('lecturesvideo/',views.lecturesvideo),
    path('stask/',views.stask),




]