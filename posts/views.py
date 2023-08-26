from django.shortcuts import render
from django.http import HttpResponse
from posts.models import Post
from django.views import generic
from django.urls import reverse_lazy

def hello(request):
    # my_list = [1, 2, 3, 4]
    body = "<h1>Hello</h1>"
    # body = """
    # <!DOCTYPE html>
    #     <html>
    #         <head>
    #             <title>Test</title>
    #         </head>
    #         <body>

    #             <h1>Заголовок 1 уровня</h1>
    #             <p>Это параграф</p>

    #         </body>         
    #     </html>
    # """
    headers = {"name": "Alex"}
            #    "Content-Type": "aplication/vnd.ms-exel",
            #    "Content-Disposition": "attachment; filename=file.xls"
    return HttpResponse(body, headers = headers, status = 500)  #



# def get_index(request):
#     posts = Post.objects.filter(status=True)
#     print(posts)
#     # print(request.__dict__)
#     # print(request.user)
#     # if request.method == "GET":
#     #     return HttpResponse("Главная страница")
#     # else:
#     #     return HttpResponse("НЕ тот метод запроса")
#     context = {
#         "title": "Главная страница",
#         "posts": posts,
#     }
#     return render(request, "posts/index.html", context = context)

# def get_about(request):
#     context = {
#         "title": "Страница о нас",
#     }
#     return render(request, "posts/about.html", context=context)




class IndexView(generic.ListView):
    queryset = Post.objects.filter(status=True)
    context_object_name = "posts"
    # model = Post
    template_name = "posts/index.html"

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"

class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }
    
class PostCtreatView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

class PostDeletView(generic.DeleteView):
    model = Post
    success_url = reverse_lazy("index-page")
    
class PostUpdateView(generic.UpdateView):
    model = Post
    template_name = "posts/post_update.html"
    fields = ["title", "content"]
    success_url = reverse_lazy("index-page")

def get_contacts(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "posts/contacts.html", context=context)

def get_post(request):
    context = {
        "title": "Создание поста",
    }
    return render(request, 'posts/post_create.html', context=context)

def update_post(request):
    context = {
        "title": "Обновление данных поста",
    }
    return render(request, 'posts/post_update.html', context=context)

def delete_post(request):
    context = {
        "title": "Удаление поста",
    }
    return render(request, "posts/post_create.html", context=context)