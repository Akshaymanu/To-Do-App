from . import views
from django.urls import path



urlpatterns = [

     path('', views.index, name='index'),
     path('update_task/<str:pk>/',views.updatetask,name='update_task'),
     path('del_item/<str:pk>/',views.deleteTask,name='del_item')

]


