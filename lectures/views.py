from django.shortcuts import render, get_object_or_404
from lectures.models import Lecture
from django.http import JsonResponse

def detail(request, lecture_slug):
    lectures = Lecture.objects.all()
    lecture = Lecture.objects.get(pk=1)
    url = lecture.video
    lectureId = url.split('=')[1]
    slug = lecture.slug

    return render(request, 'detail.html', {
        'lecture':lecture, 
        'lectures':lectures, 
        'lectureId':lectureId,
        'slug':slug,
        }
    )

def playlist_first(request, lecture_slug, lecture_id):

    lecture = Lecture.objects.get(pk=lecture_id)
    lectures = Lecture.objects.all()
    data = {}

    if lecture.is_clicked == False:
        lecture.is_clicked = True
        lecture.save()

    for lecture in lectures:

        if lecture.pk == lecture_id:
            continue

        if lecture.is_clicked == True:
            lecture.is_clicked = False
            lecture.save()

    data = {
            'title':lecture.title,
            'description':lecture.description,
            'lecturer':lecture.lecturer,
            'is_clicked':lecture.is_clicked,
            'created_at':lecture.created_at,
        }

    return JsonResponse({'data':data})

def playlist_clicked(request, lecture_slug, lecture_id):

    lecture = Lecture.objects.get(pk = lecture_id)
    lectures = Lecture.objects.all()
    data = {}

    if lecture.is_clicked == False:
        lecture.is_clicked = True
        lecture.save()

    for lecture in lectures:

        if lecture.pk == lecture_id:
            continue

        if lecture.is_clicked == True:
            lecture.is_clicked = False
            lecture.save()

    data = {
            'title':lecture.title,
            'description':lecture.description,
            'lecturer':lecture.lecturer,
            'is_clicked':lecture.is_clicked,
            'created_at':lecture.created_at,
        }

    return JsonResponse({'data':data})