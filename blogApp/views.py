from django.shortcuts import render
from django.views.generic import ListView, DetailView, \
    CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .models import Post, Advertises
# Create your views here.
class BlogListView(ListView):
    model = Post
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = Post
    template_name = 'post.html'

class BlogCreateView(CreateView):
    model = Post
    template_name = 'newPost.html'
    fields = ['title', 'author', 'body', 'language']

class BlogUpdateView(UpdateView):
    model = Post
    template_name = 'newPost.html'
    fields = ['title', 'body', 'language']

class BlogDeleteView(DeleteView):
    model = Post
    template_name = 'deletePost.html'
    success_url = reverse_lazy('home')

def homePageView(request):
    contextData = {
        'posts': Post.objects.all(),
        'ads': Advertises.objects.all()
    }
    return render(request, 'fakeHomePage.html', context=contextData)

def testCreateView(request):
    new = Post(title='CreateViewTest',
               author=request.user,
               body='Random body text',
               language='EN')
    new.save()
