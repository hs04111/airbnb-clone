"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# settings를 from . import settings로 하면 안되고, 위와 같이 한다.
# 위의 settings는 우리의 settings를 mirror한 것.


urlpatterns = [
    path("", include("core.urls", namespace="core")),
    path("rooms/", include("rooms.urls", namespace="rooms")),
    path("users/", include("users.urls", namespace="users")),
    path("admin/", admin.site.urls),
]

# 개발자 모드에서 미디어 파일들을 임시로 저장한 폴더의 url을 정해준다.
# 나중에 아마존 등에 업로드할 때에는 다른 스토리지 서버에 사용자 미디어 파일 등을 다시 저장하도록 할 것
# static을 통해 url과 디렉토리를 연결함
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
