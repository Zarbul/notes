from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from notes.models import Note, Category


class BaseView(TemplateView):
    template_name = 'base.html'

    def get(self, request, *args, **kwargs):
        category_list = Category.objects.all()
        return render(request, self.template_name, {'category_list': category_list})


class NoteListView(LoginRequiredMixin, ListView):
    template_name = 'notes/note_list.html'
    model = Note
    category_list = Category.objects.all()

    def get(self, request, *args, **kwargs):
        note_list = Note.objects.filter(author=request.user)
        return render(request, self.template_name, {'note_list': note_list, 'category_list': self.category_list})


class NoteDetailView(DetailView):
    model = Note


class NoteByCategoryView(NoteListView):

    def get(self, request, *args, **kwargs):
        note_list = Note.objects.filter(author=request.user).filter(category=kwargs['pk'])
        return render(request, self.template_name, {'note_list': note_list, 'category_list': self.category_list})
