from django.shortcuts import get_object_or_404, render, get_list_or_404
from django.utils.text import slugify
from django.views import generic

from myapp.models import Post
from myapp.forms.comment import CommentForm
from myapp.forms.post import PostForm


class PostView(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('created_on')
    template_name = 'index.html'


def post_create(request):
    template_name = "post_create.html"
    post = get_list_or_404(Post)
    new_post = None
    # Post Create
    if request.method == "POST":
        post_form = PostForm(data=request.POST)

        if post_form.is_valid():
            # Create post object but don't save to database yet
            new_post = post_form.save(commit=False)

            # AutoPopulate Slug
            new_post.slug = slugify(new_post.title)

            #  Save the comment to the database
            new_post.save()
    else:
        post_form = PostForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "new_post": new_post,
            "post_form": post_form,
        },
    )


def post_detail(request, slug):
    template_name = "post_detail.html"
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True).order_by("-created_on")
    new_comment = None
    # Comment posted
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            #  Assign the current post to the comment
            new_comment.post = post
            #  Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(
        request,
        template_name,
        {
            "post": post,
            "comments": comments,
            "new_comment": new_comment,
            "comment_form": comment_form,
        },
    )
