from django.shortcuts import render
from django.http import HttpResponse

blog_list_db = [
    {
        "id": 1,
        "title": "장고는 너무 재미있어!!!",
        "content": "This is the content of blog 1",
        "author": "Author 1",
    },
    {
        "id": 2,
        "title": "파이썬도 너무 재미있어!!!!",
        "content": "This is the content of blog 2",
        "author": "Author 2",
    },
    {
        "id": 3,
        "title": "Life is too short, You need python!",
        "content": "This is the content of blog 3",
        "author": "Author 3",
    },
]

user_list_db = [
    {
        "id": 1,
        "username": "hojun",
        "email": "hojun@gmail.com",
        "password": "1234",
    },
    {
        "id": 2,
        "username": "jihun",
        "email": "jihun@gmail.com",
        "password": "1234",
    },
    {
        "id": 3,
        "username": "junho",
        "email": "junho@gmail.com",
        "password": "1234",
    },
]


# def index(request):
#     return HttpResponse("index")

# def blog_list(request):
#     blog_list_html = ""

#     for blog in blog_list_db:
#         blog_list_html += f'<li><a href="/blog/{blog["id"]}">{blog["title"]}</a></li>'

#     return HttpResponse(f"""
#     <h1> blog list</h1>                    
#     <ul>
#         {blog_list_html}                     
#     </ul> 
#     """)

# def blog_details(request, pk):
#     blog = blog_list_db[pk-1]
#     return HttpResponse(f"""
#                 <h1> {blog['title']})</h1>
#                 <p> {blog['content']}</p>
#                 <p> {blog['author']}</p>""")

# def accounts_details(request, username):
#     finduser = None 
#     for user in user_list_db:
#         if user['username'] ==username:
#             finduser = user

#     if finduser is None:
#         return HttpResponse("User not found")
  
#     return HttpResponse(f"""
#     <h1>{finduser['username']}</h1>
#     <p>{finduser['email']}</p>
#     """)


# HttpResponse로 만들게되면 views.py파일이 너무 길어지고 유지보수 힘듦. 
# 그래서 render 방식을 사용해 http파일과 렌더링해준다. 


def index(request):
    return HttpResponse("index")

def blog_list(request):
    context = {"blog_list": blog_list_db, "hello":[10,20,30]}
    return render(request, "main/blog_list.html",context)
#context는 템플릿에 값을 전달해주기 위해 꼭 필요할 때 사용하는 것. 
# 데이터가 있다며 context를 사용해줘야 한다. 템플릿에서 파이썬 데이터를 보여줘야 하니까. 



def blog_details(request, pk):
    blog = blog_list_db[pk-1]
    context = {"blog":blog}
    return render(request, "main/blog_details.html",context)
# 특정 블로그 글 하나의 상세 페이지 코드 
# {"blog":blog}는 템플릿에서 {{blog.tilte}} 또는 {{blog.id}} 이렇게 쓸 수 있게 만들어주. 
# "blog"라는 이름을 context라는 상자에 붙여서 blog글 내용을 담아온다. 

def accounts_details(request, username):
    finduser = None 
    for user in user_list_db:
        if user["username"] == username:
            finduser = user
            break
    if finduser is None:
        return HttpResponse("User not found")
    context = {"user": finduser}
    return render(request, "main/accounts_details.html", context)

