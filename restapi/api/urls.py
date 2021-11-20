from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ServiceList
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', ServiceList.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = format_suffix_patterns(urlpatterns)
