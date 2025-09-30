from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.signup, name="signup"),
    path('formhandler', views.formhandler, name="formhandler"),
    path('profile', views.profile, name="profile")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
