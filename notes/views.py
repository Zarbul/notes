from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from notes.models import Note


class BaseView(TemplateView):
    template_name = 'base.html'


class NoteListView(ListView):
    model = Note


class NoteDetailView(DetailView):
    model = Note