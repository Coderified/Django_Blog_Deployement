from http.client import HTTPResponse
from django.shortcuts import render

from blog.models import Post
from blog.forms import PostForm
from django.db.models import Q 
# Create your views here.   

def blog_index(request):
    posts = Post.objects.all().order_by('-createdon')
    context={
        "posts":posts,
    }
    return render(request,"blog_index.html",context)

def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by(
        '-createdon'
    )
    context = {
        "category": category,
        "posts": posts
    }
    return render(request, "blog_category.html", context)

def blog_detail(request,pk):
    post = Post.objects.get(pk=pk)
    context={
        'post':post,
    }
    return render(request,'blog_detail.html',context)

def model_form(request):
    if request.method == 'POST':
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            fileis = request.FILES.get('file', None)
            if fileis is not None:
                file_name=fileis.name
                file_path='/media/'+file_name
                form.save()
                return HTTPResponse('Successful')
    else:
        form = PostForm()
        context={'form':form}
    return render(request,'model_form.html',context)    

def search(request): 
    context = {} 
    posts = Post.objects.all() 
    if request.method == "GET": 
        query = request.GET.get("search") 
        queryset = posts.filter(Q(title__icontains=query)) 
        total = queryset.count() 
        context.update({ 
            "total":total, 
            "query":query, 
            "posts":queryset, 
        }) 
 
        return render(request, "search_results.html", context) 