from django.shortcuts import render, get_object_or_404
from lectures.models import Lecture
from accounts.models import History, User
from django.http import JsonResponse


def detail(request, lecture_slug):
    lectures = Lecture.objects.all().order_by('created_at')
    lecture = Lecture.objects.get(pk=1)
    slug = lecture.slug
    
    #임의 설정
    
    if request.method == 'POST':
        #plus = request.POST.get('plus', 0)
        #email = request.POST.get('email', 0)
        if request.user.is_authenticated:
            current_user = request.user #로그인한 유저
            user_info = User.objects.filter(username = current_user.username).get()
            if 'plus' in request.POST: #임의설정; +1버튼 누르면 단순히 시청영상 갯수 +1되도록함
                user_info.lecture_count += 1
                user_info.save()
            elif 'email' in request.POST:
                user_info.email= request.POST['email']
                user_info.is_subscriber= True
                user_info.save()
            return render(request, 'detail.html', {
                'lecture':lecture, 
                'lectures':lectures, 
                'user_info':user_info,
                'slug':slug,
            })
    else:
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
