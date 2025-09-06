from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Category, Post
from .forms import PostForm

@login_required
def create_post(request):
    if request.user.user_type != 'doctor':
        return HttpResponseForbidden("Only doctors can create blog posts.")
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('blog_my_posts')
    else:
        form = PostForm()
    return render(request, 'blog_create.html', {'form': form})


@login_required
def my_posts(request):
    if request.user.user_type != 'doctor':
        return HttpResponseForbidden("Only doctors can view this.")
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog_my_posts.html', {'posts': posts})

# def blog_list(request):
#     categories = Category.objects.all()
#     # for each category, show non-draft posts
#     return render(request, 'blog_list.html', {'categories': categories})

def category_posts(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.posts.filter(is_draft=False).order_by('-created_at')
    return render(request, 'blog_category.html', {'category': category, 'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    # if it's a draft, only author (doctor) can view
    if post.is_draft and not (request.user.is_authenticated and request.user == post.author):
        return HttpResponseForbidden("This post is a draft.")
    return render(request, 'blog_detail.html', {'post': post})



def blog_list(request):
    """
    Prepare a list of categories along with their published posts
    (posts where is_draft == False). Filtering/ordering is done here
    (in Python) because Django templates cannot call .filter(...) with args.
    """
    categories = Category.objects.prefetch_related('posts').all()

    categories_with_posts = []
    for category in categories:
        posts = category.posts.filter(is_draft=False).order_by('-created_at')
        categories_with_posts.append({
            'category': category,
            'posts': posts  # queryset (possibly empty)
        })

    return render(request, 'blog_list.html', {
        'categories_with_posts': categories_with_posts
    })


