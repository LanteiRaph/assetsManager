
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', RedirectView.as_view(url='assets/')),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('onboarding/', include('onboarding.urls')),
    path('assets/', include('assets.urls')),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

