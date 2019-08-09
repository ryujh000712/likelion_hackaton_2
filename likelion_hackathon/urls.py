
from django.urls import path, include
from django.contrib import admin

import blog.views


import wordconter.views
import main.views
import portfolio.views

from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('wordcounter/', include('wordconter.urls')),
    path('blog/', include('blog.urls')),
    path('portfolio/', include('portfolio.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


