from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Post


def home(request):
    posts = Post.objects.all()
    return render(request, "posts/index.html", {"posts": posts})


def new(request):
    return render(request, "posts/new.html")


@require_POST
def create(request):
    post = Post(
        title=request.POST["title"],
        number=request.POST["number"],
        note=request.POST["note"],
    )
    post.save()
    return redirect("postes:index")


def show(request, id):
    post = get_object_or_404(Post, pk=id)
    if request.method == "POST":
        post.title = request.POST["title"]
        post.number = request.POST["number"]
        post.note = request.POST["note"]
        post.save()
        return redirect(f"/{post.id}")
    else:
        return render(request, "posts/show.html", {"post": post})


def edit(request, id):
    post = get_object_or_404(Post, pk=id)
    return render(request, "posts/edit.html", {"post": post})


@require_POST
def delete(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect("postes:index")
