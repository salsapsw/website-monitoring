from django.contrib import admin
from django.urls import path, include
import dashboard.views as views
import graph.views as graph_views
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include("dashboard.urls")),
    path("setting/", include("setting.urls")),
    path("graph/", include("graph.urls")),
    path("", include("user.urls")),
    path("profil/", include("profil.urls")),
    # path("", graph_views.get_data_to_show, name ='get_data_to_show'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)