from django.shortcuts import render, redirect
from .models import TodoItem


# Create your views here.
def todo_list(request):
    todos = TodoItem.objects.all()
    return render(request, "todo/todo_list.html", {"todos": todos})


def add_todo(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        TodoItem.objects.create(title=title, description=description)
        return redirect("todo_list")
    return render(request, "todo/add_todo.html")
