from django.http import HttpResponse,HttpResponseRedirect
from .models import todo
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.shortcuts import render
import time


def index(request):
    #template = loader.get_template("todo/index.html")  
    all_todos = todo.objects.all()         
    context = {"all_todos" : all_todos}
    #return HttpResponse(template.render(context,request))
    return render(request,'todo/index.html',context)

@csrf_exempt
def addTodo(request):
    error  = ""
    todoData = json.loads(request.body)
    localtime = time.asctime( time.localtime(time.time()) )
    if todoData.get("title") != "" and todoData.get("note") != "":
        new_todo = todo()
        new_todo.todo_title = todoData.get("title")
        new_todo.todo_note = todoData.get("note")
        new_todo.todo_date = localtime
        new_todo.save()
    else:    
        error  = "All fields compulsary"
    
    all_todos = todo.objects.all()
    context = {"all_todos" : all_todos,"error" : error}
    #return render(request,'todo/index.html',context)
    template = loader.get_template("todo/index.html")
    return HttpResponse(template.render(context,request))
    
def edit(request, todo_id):
    todo_data = todo.objects.filter(id = todo_id)
    #template = loader.get_template("todo/edit.html")
    all_todos = todo.objects.all()
    context = {"all_todos" : all_todos, "todo_data" : todo_data,}
    #return HttpResponse(template.render(context,request))
    return render(request,'todo/index.html',context)

def delete(request, todo_id):
    error = ""
    delete_todo = todo.objects.filter(id = todo_id)
    delete_todo.delete()
    #all_todos = todo.objects.all()         
    #context = {"all_todos" : all_todos,"error" : error}
    template = loader.get_template("todo/index.html")
    return HttpResponseRedirect("/todo")
    #return render(request,'todo/index.html',context)

@csrf_exempt
def update(request):
    error  = ""
    todoData = json.loads(request.body)
    localtime = time.asctime( time.localtime(time.time()) )
    if todoData.get("title") != "" and todoData.get("note") != "":
        new_todo = todo.objects.get(id = todoData.get("id"))
        new_todo.todo_title = todoData.get("title")
        new_todo.todo_note = todoData.get("note")
        new_todo.todo_date = localtime
        new_todo.save()
    else:    
        error  = "All fields compulsary"
    
    all_todos = todo.objects.all()         
    context = {"all_todos" : all_todos }
    return HttpResponseRedirect("/todo")
    #return render(request,'todo/index.html',context)

