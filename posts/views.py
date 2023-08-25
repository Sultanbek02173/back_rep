from django.shortcuts import render
from django.http import HttpResponse


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

def get_index(request):
    # print(request.__dict__)
    # print(request.user)
    # if request.method == "GET":
    #     return HttpResponse("Главная страница")
    # else:
    #     return HttpResponse("НЕ тот метод запроса")
    context = {
        "title": "Главная страница",
        "my_list": [1, 2, 3],
    }
    return render(request, "posts/index.html", context = context)
    
def get_contacts(request):
    context = {
        "title": "Контакты",
    }
    return render(request, "posts/contacts.html", context=context)

def get_about(request):
    context = {
        "title": "Страница о нас",
    }
    return render(request, "posts/about.html", context=context)