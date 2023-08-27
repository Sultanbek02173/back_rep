from typing import Any, Dict
from django.shortcuts import render, redirect
from django.http import HttpResponse

from posts.forms import CommentForm, PostForm
from posts.models import Post, Commets
from django.views import generic
from django.urls import reverse_lazy

def hello(request):
    body = "<h1>Hello</h1>"
    headers = {"name": "Alex"}
            #    "Content-Type": "aplication/vnd.ms-exel",
            #    "Content-Disposition": "attachment; filename=file.xls"
    return HttpResponse(body, headers = headers, status = 500)



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
    
    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["title"] = "Главная страница"
        return context
    

class PostDetailView(generic.DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detail.html"
    
    def post(self, request, pk):
        
        # print(request.POST)
        # post_id = request.POST.get("post_id", None) #обязательно до переменной post
        post = Post.objects.get(pk=pk) #pk=post_id и добавить input hidden
        
        form = CommentForm(request.POST)
        
        # name = request.POST.get("name", None)
        # text = request.POST.get("text", None)
        
        # if name and text:
        #     comment = Commets.objects.create(name = name, text = text, post = post)
        #     comment.save()
            
        if form.is_valid():
            pre_saved_comment = form.save(commit=False) #пока не отправлять к бд
            pre_saved_comment.post = post
            pre_saved_comment.save()
              
        return redirect("detailPost-page", pk)

    def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["title"] = "Просмотр поста"
        return context

class AboutView(generic.TemplateView):
    template_name = "posts/about.html"
    extra_context = {
        "title": "Страница о нас",
    }
    
class PostCtreatView(generic.CreateView):
    model = Post
    template_name = "posts/post_create.html"
    # fields = ["title", "content"]
    success_url = reverse_lazy("index-page")
    form_class = PostForm
    

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

# def get_post(request):
#     context = {
#         "title": "Создание поста",
#     }
#     return render(request, 'posts/post_create.html', context=context)

# def update_post(request):
#     context = {
#         "title": "Обновление данных поста",
#     }
#     return render(request, 'posts/post_update.html', context=context)

# def delete_post(request):
#     context = {
#         "title": "Удаление поста",
#     }
#     return render(request, "posts/post_create.html", context=context)