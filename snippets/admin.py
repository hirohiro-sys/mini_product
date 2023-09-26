from django.contrib import admin
from snippets.models import Snippet,Comment

# モデル登録
admin.site.register(Snippet)
admin.site.register(Comment)