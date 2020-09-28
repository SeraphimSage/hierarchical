from django.shortcuts import render, HttpResponseRedirect, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from hierarchical_app.models import Folder
# from hierarchical_app.models import MyUser
# from hierarchical_app.forms import LoginForm, SignupForm, MyUserForm, FolderForm
from django.views.generic import TemplateView
# Create your views here.

def index_view(request):
    # if request.user.id:
    #     folder = Folder.objects.filter(myuser__id=request.user.id)
    # else:
    #     folder = Folder.objects.all()
    return render(request, "index.html", {"folder": Folder.objects.all()})

# class LoginView(TemplateView):
#     def get(self, request):
#         form = LoginForm()
#         return render(request, "generic_form.html", {"form": form})

#     def post(self, request):
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             user = authenticate(request, username=data.get("username"), password=data.get("password"))
#             if user:
#                 login(request, user)
#                 return HttpResponseRedirect(request.GET.get('next', reverse("homepage")))
#             else:
#                 return render(request, "generic_form.html", {"form": form})

# class LogoutView(TemplateView):
#     def get(self, request):
#         logout(request)
#         return HttpResponseRedirect(reverse("homepage"))

# class SignupView(TemplateView):
#     def get(self, request):
#         form = SignupForm()
#         return render(request, "generic_form.html", {"form": form})

#     def post(self, request):
#         form = SignupForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             new_user = MyUser.objects.create_user(
#                 username=data.get("username"),
#                 password=data.get("password"),
#                 display_name=data.get("display_name"))
#             login(request, new_user)
#             return HttpResponseRedirect(reverse("homepage"))

#         else:
#             return render(request, "generic_form.html", {"form": form})

# class CreateView(TemplateView):
#     @login_required
#     def post(self, request):
#         form = FolderForm(request.POST)
#         if form.is_valid():
#             data = form.cleaned_data
#             author = MyUser.objects.filter(user__id=request.user.id).first()
#             new_folder = Folder.objects.create(
#                 name = data['name'],
#                 parent = data['parent'],
#                 creator = author
#             )
#             if new_folder:
#                 return HttpResponseRedirect(reverse('homepage'))
        
#         form = FolderForm()
#         return render(request, 'create.html', {'form': form})
