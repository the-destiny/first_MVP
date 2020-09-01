from django.shortcuts import render, get_object_or_404
from lectures.models import Lecture

# Create your views here.

def detail(request, lecture_slug):

    lecture = get_object_or_404(Lecture, slug=lecture_slug)

    return render(request, 'detail.html', {'lecture':lecture})