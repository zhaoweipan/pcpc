from django.urls import path

from . import views



#generic view

app_name='sightings'
urlpatterns=[
    path('',views.IndexView,name='sightings'),
    path('',views.DeleteView,name='delete'),
    path('stats/',views.StatsView,name='stats'),
    path('add/',views.AddView,name='add'),    
    path('<Unique_Squirrel_Id>/',views.UpdateView,name='update'),
    path('',views.DeleteView,name='delete'),
    
    ]
