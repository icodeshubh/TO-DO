"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from myapp import views
from myapp import forms

urlpatterns = [

    path('admin/', admin.site.urls),
    # path('add/',views.add,name='add'),
    path('',views.index,name='index'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('edit/<int:id>/',views.update,name='update'),
    path('cbvindex/',views.TaskListView.as_view(),name='cbvindex'),
    path('cbvdetail/<int:pk>/',views.DetailListView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.UpdateListView.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.DeleteListView.as_view(),name='cbvdelete'),

]
