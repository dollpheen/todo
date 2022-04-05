from django.shortcuts import render
from django.http import HttpResponse
from random import shuffle
from django import forms

def action(request,main):
    if main[-1] == '0':
        code = main[:-1]
        file = open(f'data/todos/{code}','a+')
        file.write('\n'+str(request.POST['to_add']))
        file.close()
        return todolist(request,code)
    elif main[-1] == '1':
        code = main[:-1]
        try:
            file = open(f'data/todos/{code}','r')
            list = file.read().split('\n')
            list.pop(int(request.POST['delete']))
            file.close()
            file = open(f'data/todos/{code}','w')
            file.write('\n'.join(list))
            file.close()
            return todolist(request,code)
        except:
            return todolist(request,code)
    else:
        return HttpResponse('edit')
def create(request):
    total = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','3','4','5','6','7','8','9']
    shuffle(total)
    to_return = ''.join(total[:8])
    file = open('data/users' ,'a+')
    while True:
        if to_return in file.read():
            shuffle(total)
            to_return = ''.join(total[:8])
        else:
            file.write(to_return+'\n')
            file.close()
            fp = open(f'data/todos/{to_return}', 'x')
            fp.close()
            return HttpResponse(f"<h2>User sucessfully created </h2><h3 style='color:green'>{to_return}</h3><p>    This is your account code for the todo app copy it and goto login </p><a href='/login'>login</a>")
def login(request):
    context = {}
    return render(request, "login.html", context)
def todolist(request,code=''):
    if request.method == 'POST' or code:
        file = open('data/users','r')
        if code:
            pass
        else:
            code = request.POST['code']
        if code in file.read():
            file.close()
            file2 = open(f'data/todos/{code}','r')
            list = file2.read().split('\n')
            file2.close()
            final_List = [value for value in list if value != ""]
            context = {'code':code,'todo':final_List}
            return render(request, "todo.html",context)
        else:
            file.close()
            return HttpResponse("<h2>User not found</h2><a href='/create'>create user</a>")
    else:
        return HttpResponse("<h2>Welcome to TODO!</h2><a href='/create'>create user</a><a href = '/login' ><p>login</p></a>")
