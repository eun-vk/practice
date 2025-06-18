from django.shortcuts import render
from django.http import HttpResponse, Http404

def index(request):
    return HttpResponse("안녕하세요! 메인 페이지입니다.")

# chat/urls.py에서 name인자를 추출해서 
# view 함수 호출 시에 자동으로 인자를 전달해줍니다. 

def puzzle_room(request, name):

    try: 
        image_url = {
        "mario": "/static/chat/mario.jpg",
        "toy": "/static/chat/toy-story.jpg",
        "openai-1": "/static/chat/sun.png",
        "openai-2": "/static/chat/image.png",
    }[name]

    except KeyError:
        raise Http404(f"not found room: {name}")
    
    level=3
    
    return render(
        request,
        template_name="chat/puzzle.html",

        context={"image_url":image_url, "level":level},
    )
def chat_message_new(request):
    # 새로운 메시지 작성 페이지 또는 처리 로직 작성
    return HttpResponse("새 메시지 작성 페이지입니다.")
