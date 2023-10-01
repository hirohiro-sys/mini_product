from django.urls import path
from snippets.views import (
    SnippetNewView,
    SnippetEditView,
    SnippetDetailView,
    CommentNewView,

)

# エラーページカスタマイズ
handler400 = 'snippets.views.handler400'
handler403 = 'snippets.views.handler403'
handler404 = 'snippets.views.handler404'
handler500 = 'snippets.views.custom_500'


urlpatterns = [
    path("new/", SnippetNewView.as_view(), name="snippet_new"),
    path("<int:snippet_id>/", SnippetDetailView.as_view(), name="snippet_detail"),
    path("<int:snippet_id>/edit/", SnippetEditView.as_view(), name="snippet_edit"),
    path("<int:snippet_id>/comments/", CommentNewView.as_view(), name="comment_new"),
]

