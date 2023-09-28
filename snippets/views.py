from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.core.exceptions import PermissionDenied
from snippets.forms import SnippetForm, CommentForm
from snippets.models import Snippet, Comment

class TopView(View):
    def get(self, request):
        snippets = Snippet.objects.all()
        context = {"snippets": snippets}
        return render(request, "snippets/top.html", context)

class SnippetNewView(View):
    @method_decorator(login_required)
    def get(self, request):
        form = SnippetForm()
        return render(request, "snippets/snippet_new.html", {'form': form})

    @method_decorator(login_required)
    def post(self, request):
        form = SnippetForm(request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.created_by = request.user
            snippet.save()
            messages.add_message(request, messages.SUCCESS,
                                 "スニペットを作成しました。")
            return redirect('snippet_detail', snippet_id=snippet.pk)
        else:
            messages.add_message(request, messages.ERROR,
                                 "スニペットの作成に失敗しました。")
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
