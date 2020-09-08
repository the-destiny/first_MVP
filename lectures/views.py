from django.shortcuts import render, get_object_or_404
from lectures.models import Lecture
from django.http import JsonResponse


def detail(request, lecture_slug):
    lectures = Lecture.objects.all().order_by('created_at')
    lecture = Lecture.objects.get(pk=1)
    slug = lecture.slug
    return render(request, 'detail.html', {
        'lecture':lecture, 
        'lectures':lectures, 
        'slug':slug,
        }
    )
  
  
def listup(request):
    return render(request, 'listup.html')

  
def listup_categ(request):
    return render(request, 'listup_categ.html')
  
  
def playlist_first(request, lecture_slug, lecture_id):
    lecture = Lecture.objects.get(pk=lecture_id)
    lectures = Lecture.objects.all()
    url = lecture.video
    lectureId = url.split('=')[1]
    data = {}
    if lecture.is_clicked == False:
        lecture.is_clicked = True
        lecture.save()
    for item in lectures:
        if item.pk == lecture_id:
            continue
        if item.is_clicked == True:
            item.is_clicked = False
            item.save()
    data = {
        'title':lecture.title,
        'description':lecture.description,
        'lecturer':lecture.lecturer,
        'is_clicked':lecture.is_clicked,
        'created_at':lecture.created_at,
        'lectureId' : lectureId,
    }
    return JsonResponse({'data':data})

  
def playlist_clicked(request, lecture_slug, lecture_id):
    lecture = Lecture.objects.get(pk = lecture_id)
    lectures = Lecture.objects.all()
    url = lecture.video
    lectureId = url.split('=')[1]
    data = {}
    if lecture.is_clicked == False:
        lecture.is_clicked = True
        lecture.save()
    for item in lectures:
        if item.pk == lecture_id:
            continue
        if item.is_clicked == True:
            item.is_clicked = False
            item.save()
    data = {
        'title':lecture.title,
        'description':lecture.description,
        'lecturer':lecture.lecturer,
        'is_clicked':lecture.is_clicked,
        'created_at':lecture.created_at,
        'lectureId' : lectureId,
    }
    return JsonResponse({'data':data})
