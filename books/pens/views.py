from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST
from .models import Pen
from .forms import PenForm
from django.contrib import messages


# Create your views here.

def index(req):
    pens = Pen.objects.all()
    return render(req, "pens/index.html", {"pens": pens})


def show(req, id):
    pen = get_object_or_404(Pen, pk=id)
    if req.method == "POST":
        # form = PenForm(req.POST)  # 我要新增的東西
        # form = PenForm(instance=pen)  # 目前有的東西
        form = PenForm(req.POST, instance=pen)
        if form.is_valid():
            form.save()
        # return redirect(f"/{pen.id}")
        return redirect("pens:show", id=pen.id)
    else:
        return render(req, "pens/show.html", {"pen": pen})


def new(req):
    form = PenForm()  # 建立表單物件
    return render(req, "pens/new.html", {"form": form})


@require_POST
def create(req):
    form = PenForm(req.POST)  # 建立表單，把整坨東西餵給他
    if form.is_valid():  # 是否是有效的（某個欄位是必填），在model之前就先做篩選
        form.save()  # 驗證過就叫表單存檔

        messages.success(req, "新增成功！")  # 新增成功的訊息，只會出現一次（規則）

    return redirect("pens:index")


def edit(req, id):
    pen = get_object_or_404(Pen, pk=id)
    form = PenForm(instance=pen)
    return render(req, "pens/edit.html", {"pen": pen, "form": form})
    # 注意！render 函數只接受一個字典函數


@require_POST
def delete(req, id):
    pen = get_object_or_404(Pen, pk=id)
    pen.delete()
    messages.error(req, "資料已刪除！")
    return redirect("pens:index")
