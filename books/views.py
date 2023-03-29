from books.models import Book
from django.views.generic import ListView,DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
# Create your views here.

class BookList(ListView):
    model=Book
    template_name='books/book_lists.html'

class BookView(DetailView):
    model=Book
    template_name='books/book_detail.html'

class BookCreate(CreateView):
    model=Book
    template_name='book_new.html'
    fields=['name','pages']
    success_url=reverse_lazy('book_list')

class BookUpdate(UpdateView):
    model=Book
    template_name='books/book_edit.html'
    fields=['name','pages']
    success_url=reverse_lazy('book_list')

class BookDelete(DeleteView):
    model=Book
    template_name='books/book_delete.html'
    success_url=reverse_lazy('book_list')
