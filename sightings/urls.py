from django.urls import path
from . import views
#generic view
app_name='sightings'
urlpatterns=[
    path('',views.all_squirrels),
    path('',views.DeleteView),
    path('stats/',views.StatsView),
    path('add/',views.AddView),
    path('<Unique_Squirrel_Id>/',views.UpdateView),
]

