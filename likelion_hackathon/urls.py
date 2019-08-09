
from django.urls import path, include
import blog.views, wordconter.views, portfolio.views, main.views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('wordcounter/', include('wordconter.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


