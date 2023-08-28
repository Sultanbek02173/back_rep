from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy

from .forms import UserReqistrationForm

from users.serializers import UserSerializer
from rest_framework import generics
from .models import CustomUser



class UserListView(generics.ListAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()


class UserDetailAPIView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    queryset = CustomUser.objects.all()
    lookup_field = "id"








class UserRegister(generic.CreateView):
    form_class = UserReqistrationForm
    success_url = reverse_lazy("login")
    template_name = "registration/register.html"
    
    def post(self, request):
        user_form = UserReqistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, "registration/register_done.html", {"user": new_user})
        return render(request, "registration/register.html", {"form": user_form})


# def register(request):
#     if request.method == "POST":
#         user_form = UserReqistrationForm(request.POST)
#         if user_form.is_valid():
#             new_user = user_form.save(commit=False)
#             new_user.set_password(user_form.cleaned_data['password'])
#             new_user.save()
#             return render(request, "registration/register_done.html", {"user": new_user})
#     else:
#         user_form = UserReqistrationForm()
#     return render(request, "registration/register.html", {"form": user_form})
