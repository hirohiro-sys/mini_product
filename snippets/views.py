from typing import Any
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models.query import QuerySet
from django.db.models import Q 
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView
from django.urls import reverse_lazy
from django.core.exceptions import PermissionDenied
from urllib.parse import quote

from snippets.forms import SnippetForm, CommentForm
from snippets.models import Snippet, Comment


# ページネーション、検索機能、更新日でソート機能実装
class TopView(ListView):
    model = Snippet
    template_name = "snippets/top.html"
    context_object_name = "snippets"
    paginate_by = 8

    def get_queryset(self):
         queryset = Snippet.objects.all().order_by('-updated_at')
         query = self.request.GET

         
         if q := query.get('q'):
             queryset = queryset.filter(Q(code__icontains=q)|Q(title__icontains=q))

         return queryset.order_by('-updated_at')
    

class SnippetNewView(View):
    @method_decorator(login_required)  # ログインが必要な場合はこのデコレータを使う
    def get(self, request):
        form = SnippetForm()
        return render(request, "snippets/snippet_new.html", {'form': form})

    @method_decorator(login_required)  # ログインが必要な場合はこのデコレータを使う
    def post(self, request):
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            messages.add_message(request, messages.SUCCESS, "スニペットを作成しました。")
            return redirect('snippet_detail', snippet_id=snippet.pk)
        else:
            messages.add_message(request, messages.ERROR, "スニペットの作成に失敗しました。")
            return render(request, "snippets/snippet_new.html", {'form': form})
        

class SnippetEditView(View):
    @method_decorator(login_required)
    def get(self, request, snippet_id):
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        if snippet.created_by_id != request.user.id:
            raise PermissionDenied("このスニペットの編集は許可されていません。")

        form = SnippetForm(instance=snippet)
        return render(request, 'snippets/snippet_edit.html', {'form': form})

    @method_decorator(login_required)
    def post(self, request, snippet_id):
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        if snippet.created_by_id != request.user.id:
            raise PermissionDenied("このスニペットの編集は許可されていません。")

        form = SnippetForm(request.POST, instance=snippet)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS,
                                 "スニペットを更新しました。")
            return redirect('snippet_detail', snippet_id=snippet_id)
        else:
            messages.add_message(request, messages.ERROR,
                                 "スニペットの更新に失敗しました。")
            return render(request, 'snippets/snippet_edit.html', {'form': form})
        

class SnippetDetailView(View):
    @method_decorator(login_required)
    def get(self, request, snippet_id):
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        comments = Comment.objects.filter(commented_to=snippet_id).all()
        comment_form = CommentForm()
        return render(request, "snippets/snippet_detail.html", {
            'snippet': snippet,
            'comments': comments,
            'comment_form': comment_form,
        })
    

class CommentNewView(View):
    @method_decorator(login_required)
    def post(self, request, snippet_id):
        snippet = get_object_or_404(Snippet, pk=snippet_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.commented_to = snippet
            comment.commented_by = request.user
            comment.save()
            messages.add_message(request, messages.SUCCESS,
                                 "コメントを投稿しました。")
        else:
            messages.add_message(request, messages.ERROR,
                                 "コメントの投稿に失敗しました。")
        return redirect('snippet_detail', snippet_id=snippet_id)
    

# エラーページカスタマイズのビュー
def handler400(request, exception):
    return render(request, 'erros/400.html', {}, status=400)

def handler403(request, exception):
    return render(request, 'erros/403.html', {}, status=403)

def handler404(request, exception):
    context = {"request_path": quote(request.path)}
    return render(request, 'erros/404.html', {}, status=404)

def custom_500(request):
    # カスタムの500エラーページを表示するためのコードを追加
    return render(request, 'custom_500.html', status=500)