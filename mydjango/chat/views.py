from django.http import HttpRequest, HttpResponse
from django.shortcuts import render




# django view : http 요청을 받아 요청을 처리하는 함수
#  - 항상 1개 인자가 있고, request를 통해 모든 요청 내역을 조회 가능


    # request에 query parameters, form data, files, headers, etc.이 들어가 있음. 

    #html_str = "<html><head></head><body><h1>hello django in html</h1></body>"


    #str (html, text), image data, pdf data, streaming, etc.
    #return HttpResponse(html_str)

# 채팅 기본 화면
def index(request: HttpRequest) -> HttpResponse:
    return render(request, "chat/index.html")

# 매 채팅 메시지를 받아, 응답 메시지를 만들고, 응답하겠어요.
# HTTP Methods : GET, POST, PUT/PATCH, DELETE, OPTIONS
#  - <form method=""> 태그(유저로부터 입력을 받아 지정 서버로 전송)에서는 GET, POST 만 지원
#  - JS API를 통해서 PUT/PATCH, DELETE 등의 요청을 할 수 있어요. 
# chat/views.py 에 추가

def chat_message_new(request: HttpRequest) -> HttpResponse:
    # Query Parameters
    request.GET   # QueryDict 타입 (Dict 으로 보여도 90% 무방)  # POST 요청에서도 있을 수 있어요.
    request.POST  # POST 데이터 (QueryDict)
    
    question = request.POST.get("question", "")
    if question:
        answer = f"당신의 질문 : {question}"
    else:
        answer = "질문이 없으시네요."

    return HttpResponse(answer)
    return render(request, "chat/index.html")

# + url encoding = "key=value&key&value=key&value"
# + url encoding 문자열이 요청 주소 뒤에 물음표(?) 뒤에 붙으면 => 그걸 Query Parameters
# + https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=0&ie=utf8&query=python&ackey=4rvenuph

"""
where=nexearch
sm=top_hty
fbm=0
ie=utf8
query=python
ackey=4rvenuph
""" 
