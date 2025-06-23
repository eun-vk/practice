from django.shortcuts import render
from django.http import HttpResponse

# url에 대응할 뷰 함수 만들기 
# config/settings.py에서 앱 등록 
# -> config/urls.py에서 url등록 
# -> main/views.py에서 각 url에 대응되는 뷰함수 만들기 
# -> 01_3_basic/main 폴더에 templates/main 폴더 생성, html파일 생성
# -> main/views.py(렌더링)수정(템플릿 html파일과 연결)
# -> 각 html 파일에 기본 정보를 입력해준다. 

'''HttpResponse 사용 '''
# def index(request):
#     return HttpResponse("<h1> 메인 페이지입니다. </h1>")

# def a(request):
#     return HttpResponse("<h1> a 페이지입니다. </h1>")

# def b(request):
#     return HttpResponse("<h1> b 페이지입니다. </h1>")

# def c(request):
#     return HttpResponse("<h1> c 페이지입니다. </h1>")

# def hojun(request):
#     return HttpResponse("<h1> 이호준 소개 페이지입니다. </h1>")

# def orm(request):
#     return HttpResponse("<h1> orm 소개 페이지입니다. </h1>")

'''render 사용하여 템플릿 렌더링 '''
#render(request 객체, 렌더링할 템플릿의 경로) -> 두 개의 매개변수를 받음.
def index(request):
    return render(request, "main/index.html")

def a(request):
    return render(request, "main/a.html")


def b(request):
    return render(request, "main/b.html")


def c(request):
    return render(request, "main/c.html")


def hojun(request):
    return render(request, "main/hojun.html")


def orm(request):
    return render(request, "main/orm.html")
