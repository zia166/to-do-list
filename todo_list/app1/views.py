from pydoc_data.topics import topics
from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect, render
from .models import Topic, Task
from django.db.models import Q
from .form import CreateForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def loginPage(request):
    page = "login"
    if request.method == "POST":
        username = request.POST.get("username").lower()
        password = request.POST.get("password")

        try:
            user = User.objects.get(username=username)
        # except Exception as e:
        #     print(e)
        except:
            messages.error(request, "User does not exists")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("profile", pk=user.id)
        else:
            messages.error(request, "Username or password does not exists")

    context = {"page": page}
    return render(request, "app1/login-registeration.html", context)


def logOutUser(request):
    logout(request)
    return redirect("login")


def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            return redirect("profile", pk=user.id)
        else:
            messages.error(request, "An error has occured durning registering")
    return render(request, "app1/login-registeration.html", {"form": form})


def userProfile(request, pk):
    q = request.GET.get("q") if request.GET.get("q") != None else ""
    tasks = Task.objects.filter(Q(topic__name__icontains=q) | Q(task__icontains=q))
    user = User.objects.get(id=pk)
    task = user.task_set.all()
    topics = user.topic_set.all()
    task_count = task.count()
    context = {"user": user, "tasks": tasks, "task_count": task_count, "topics": topics}
    return render(request, "app1/profile.html", context)





def create_task(request):
    form = CreateForm()
    user = request.user
    topics = Topic.objects.all()
    if request.method == "POST":
        topic_name = request.POST.get("topic")
        topic, created = Topic.objects.get_or_create(name=topic_name,user=user)
        Task.objects.create(
            user=request.user, topic=topic, task=request.POST.get("task")
        )
       
        return redirect("profile", pk=user.id)
    context = {"form": form, "topics": topics}
    return render(request, "app1/create_form.html", context)


def delete_task(request, pk):
    user = request.user
    task = Task.objects.get(id=pk)
    print(task)
    print(task.topic)
    topic =Topic.objects.filter(name=task.topic)
   
    if request.method == "POST":
        task.delete()
        topic.delete()

        return redirect("profile", pk=user.id)
    return render(request, "app1/delete.html", {"obj": task})
