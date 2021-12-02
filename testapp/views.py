from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Blog
from django.views import generic
from .forms import AddPostForm
class BlogView(generic.ListView):
    template_name = 'testapp/Home.html'
    context_object_name = 'blogpost'
    def get_queryset(self):
        return Blog.objects.all()

class BlogDetail(generic.DetailView):
    model = Blog
    template_name = 'testapp/BlogDetail.html'


def AddPost(request):
        if request.method=="POST":
            form = AddPostForm(request.POST , request.FILES)
            if form.is_valid():
                title = form.cleaned_data['title']
                content = form.cleaned_data['content']
                image = form.cleaned_data['image']
                author = request.user 
                blog = Blog.objects.create(title = title , content = content , author = author , image = image)
                return HttpResponse("post created")
        else:
            form = AddPostForm()
            blog = Blog.objects.all()
        context = {"form" : form}
        return render(request , 'testapp/additem.html' , context)            

def PostLike(request , postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            return HttpResponse ('you already liked that post')
        else:    
            post.likes.add(user)
            return redirect ('detail' , postid)
    else:
        return HttpResponse ('you are not allow to like this post')

def PostUnlike(request , postid):
    post = Blog.objects.get(id = postid)
    user = request.user
    if user.is_authenticated:
        if user in post.likes.all():
            post.likes.remove(user)
            return redirect ('detail' , postid)
        else:
            return HttpResponse ('you are not like this post')    
    else:
        return HttpResponse ('you are not allow to like this post')