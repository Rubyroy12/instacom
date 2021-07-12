from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('instagram.urls')),
    path('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('django_registration.backends.one_step.urls')),

]
