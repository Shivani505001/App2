from django.shortcuts import render,redirect
from django.http import HttpResponse
from trydjango.models import article
import random
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required 
from .forms import allforms,allforms_model

# Create your views here.

@login_required  # decorator- which allows user to access this onli if they are authenticated 
#LOGIN_URL=[
#     '/login/'
# ] - add this in settings.py so that it will replace the default url 
def home_view(request): #take in request - as in django sends request and the below line sends a response 
    #if request.user.is_authenticated  - can use this but this line has to run always 
    random_id=random.randint(1,2)
    article_obj=article.objects.get(id=random_id)
    # article_list=
    mylist_num=article.objects.all()
    # print(id)
    #list(range(1,10))
    
    
    context = { #make a dictionary 
        "mylist":mylist_num,
        "object":article_obj,   
        "title" : article_obj.title,
        "content" : article_obj.content,
        "id" : article_obj.id
    }
    
    #method 1
    # htmlstring=f"""
    # <h1> {article_obj.title} </h1>
    # """
    # htmlpara=f"""
    # <p1>{article_obj.content}"""
    # htmls=htmlstring+htmlpara
    
    #method 2
    
    #htmls=render_to_string('home.html',context=context)
    # htmls=f"""
    # <h1>{title} {id}</h1>
    # <p>{content}</p>
    # """.format(**context)
    
    #showing list
   
    return render(request,'home.html',context)

def article_view (request,id=None):
    article_obj=None 
    if id is not None:
        article_obj=article.objects.get(id=id)
    context={
        "object":article_obj,
    }
    return render(request,'detail.html',context=context)

def search_view(request):
    # print(request.GET)
    query_dict=request.GET #this is the dictionary 
    #query=query_dict.get("q") #requesting data ,  <input type='text', name='q'> #basically taking id which is given in search box 
    try:  
        query=int(query_dict.get("q"))
    except:
        query=None
   
    article_obj=None
    if query is not None:
        article_obj=article.objects.get(id=query)#getting the taken id to get its object
    
    context={
        "object":article_obj
    }#by sending this context in search.html will print the title of required obj[see in template]
    return render(request,"search.html",context=context) 

def create_view(request):
    form=allforms_model(request.POST or None) #using django forms we r just creating a class and we r rendering that class here [like basically request.get]
    #print(dir(form))
    context={
        'form':form
    }
    # print(request.POST)
    # if request.method == 'POST':
    #     form=allforms(request.POST) #sending all the data - uncleaned data #for every newly created article the title and content comes into this instance
    if form.is_valid(): #if the data is cleaned or if the data is valid, then onli we r gonna create
        article_object=form.save()
        # title=request.POST.get('title')
        # content=request.POST.get('content')
        #    # print(title,content)
        # if title:
        #     article_object=article.objects.create(title=title,content=content)
        # context['object']=article_object
        # context['created']=True
    
        context['object']=allforms_model()
        return redirect('homes', id=article_object.id)
    
    
    return render(request,'create.html',context)
