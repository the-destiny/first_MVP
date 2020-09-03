from django.shortcuts import render, get_object_or_404
from lectures.models import Lecture


def detail(request, lecture_slug):
    lecture = get_object_or_404(Lecture, slug=lecture_slug)
    url = lecture.video
    lectureId = url.split('=')[1]
<<<<<<< HEAD
<<<<<<< HEAD
=======

>>>>>>> 10b88e5... [#6] Implement detailpage
=======
>>>>>>> e773534... [#6] Correct code
    return render(request, 'detail.html', {'lecture':lecture, 'lectureId':lectureId})
