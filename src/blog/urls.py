from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from accounts.views import signup
from blog import settings


urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('blog/', include('posts.urls')),
                  path('trap/', include('traps.urls')),
                  path('compte/nouveau/', signup, name="signup"),
                  path("compte/", include("django.contrib.auth.urls"))
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # permet de lier nos url des media au image. sans quoi l'mage ne peut pas sortir.
