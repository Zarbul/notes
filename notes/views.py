from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

# Create your views here.
from notes.models import Note


class BaseView(TemplateView):
    template_name = 'base.html'


class NoteListView(LoginRequiredMixin, ListView):
    template_name = 'notes/note_list.html'
    model = Note

    def get(self, request, *args, **kwargs):
        query = Note.objects.filter(author=request.user)
        return render(request, self.template_name, {'note_list': query})


class NoteDetailView(DetailView):
    model = Note
