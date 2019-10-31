from django.contrib import admin 
from django.urls import path, include
from mystorage import urls 
from rest_framework import urls 
from django.conf import settings 
from django.conf.urls.static import static # static 함수 사용

urlpatterns = [
	path('admin/', admin.site.urls),
	path('', include('mystorage.urls')),
	path('api-auth/', include('rest_framework.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # urlpatterns에 media가 추가될 수 있도록, 인자로는 media파일의 url과 경로를 지정한다.
