"""margin_notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path, include
from .views import BaseView, NoteListView, NoteDetailView, NoteByCategoryView

urlpatterns = [
    path('', BaseView.as_view(), name='home'),
    path('note_list/', NoteListView.as_view(), name='list'),
    path('category/<int:pk>', NoteByCategoryView.as_view(), name='category'),
    path('note_detail/<int:pk>', NoteDetailView.as_view(), name='detail'),
]
