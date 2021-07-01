from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView

from .models import Post
from .forms import EmailPostForm


def post_share(request, post_id):
    template_name = 'blog/post/share.html'
    post = get_object_or_404(Post, post_id, status='published')
    if request.method == 'POST':
        form = EmailPostForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
    else:
        form = EmailPostForm()
    return render(request, template_name, {'post': post, 'form': form})


class PostListView(ListView):
    queryset = Post.objects_published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    
# def post_list(request):
#     paginator = Paginator(posts, 3)
#     object_list = {'page': request.GET.get('page')}
#     try:
#         object_list['posts'] = paginator.page(object_list['page'])
#     except PageNotAnInteger:
#          object_list['posts'] = paginator.page(1)
#     except EmptyPage:
#         object_list['posts'] = paginator.page(paginator.num_pages)
#     return render(request, template_name, object_list)

def post_detail(request, year, month, day, post):
    template_name = 'blog/post/detail.html'
    object_list = {'post': get_object_or_404(
        Post,
        slug=post,
        status='published',
        publish__year=year,
        publish__month=month,
        publish__day=day,
    )}
    return render(request, template_name, object_list)