from authentication.models import Uzer
from django.shortcuts import render
from stories.models import Book
from django.contrib.auth.decorators import login_required
from authentication.models import Uzer

# Create your views here.


@login_required
def index_view(request):
    book = Book.objects.all()
    return render(request, 'index.html', {'book': book})


def user_detail(request, user_id):
    user = Uzer.objects.get(id=user_id)
    books = Book.objects.filter(author=user)
    return render(request, 'profile.html', {'book': books})
