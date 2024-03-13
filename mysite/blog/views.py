from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
from django.template import loader
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from blog.models import Post
from django.contrib.auth.models import User
from blog.forms import CreatePostForm, CommentForm

# Create your views here.


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'all_posts'

    def get_queryset(self):
        return Post.objects.all().order_by('-created_at')

# Templates
def index(request): # last 3
    posts = Post.objects.all().order_by('-created_at')
    # template = loader.get_template('blog/index.html')
    content = {
        'all_posts' : posts
    }
    # response = (f"<ul>"
    #             f"{''.join([f'<li>{post.title}</li>' for post in posts])}"
    #             f"</ul>")
    # return HttpResponse(response)
    # return HttpResponse(template.render({}, request))  #1
    return render(request, 'blog/index.html', content)



class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/detail.html'
    context_object_name = 'post'

    def get_object(self):
        post_id = self.kwargs.get('post_id')
        return Post.objects.get(pk=post_id)


def detail(request, post_id): # параметр пути
    p = Post.objects.get(id=post_id)
    return render(request, 'blog/detail.html', {'post': p})


class PostCreateView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    success_url = reverse_lazy('index')
    form_class = CreatePostForm

    def form_valid(self, form):
        print("form instance", form.instance.id)
        form.instance.author_id = 1
        return super().form_valid(form)

# Forms
def new_post(request):
    if request.method == 'POST':
        form = CreatePostForm(request.POST)

        if form.is_valid():

            post = form.save(commit=False)
            post.author_id = 1
            post.save()

            return redirect("index")
        else:
            return HttpResponse('Error creating!')

    # GET
    context = {
        'form': CreatePostForm()
    }

    return render(request,
                  'blog/create_post.html',
                  context=context)


def add_comment(request, post_id):
    post = Post.objects.get(pk=post_id)
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            admin_user = User.objects.get(username='admin')
            comment.author = admin_user
            comment.save()
            return redirect('detail', post_id=post_id)
    else:
        form = CommentForm()
    return render(request, 'blog/add_comment.html', {'form': form})