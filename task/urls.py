from django.urls import path
from . import views
urlpatterns = [
    path('' , views.home , name='home'),
    path('complete/<int:id>/', views.taskcompleted , name="taskcompleted"),
    path('delete/<int:id>/', views.delete , name='delete'),

]