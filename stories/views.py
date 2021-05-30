from django.http.response import HttpResponseRedirect
from django.shortcuts import render, reverse
from stories.models import Book
from stories.forms import BookForm, ChapterForm

# Create your views here.


def Create_Book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            new_book = Book.objects.create(
                title=data['title'], author=request.user)
            return HttpResponseRedirect(reverse('home'))

    form = BookForm()
    return render(request, 'createbook.html', {'form': form})


def upload_chapter(request):
    if request.method == 'POST':
        form = ChapterForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(request.GET.get('next', reverse('home')))

    form = ChapterForm()
    return render(request, 'createbook.html', {'form': form})
