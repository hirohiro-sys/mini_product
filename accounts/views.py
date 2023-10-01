from django.contrib import messages
from django.contrib.auth import logout
from django.shortcuts import redirect

def custom_logout(request):
    # ユーザーにメッセージを表示
    messages.success(request, "ログアウトしました。")
    # ログアウト処理
    logout(request)
    # ログアウト後にリダイレクトする場所を指定
    return redirect('/')  


