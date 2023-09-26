from django.contrib import admin
from django.urls import path, include
from snippets.views import top

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', top, name='top'),
    path('snippets/', include('snippets.urls')),   # snippets/urlを読み込めるようにする
    path("accounts/", include("accounts.urls")),
]
