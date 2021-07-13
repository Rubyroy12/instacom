from django.contrib import admin
from django.conf.urls import url,include
from django.contrib.auth import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django_registration.backends.one_step.views import RegistrationView


urlpatterns = [
    url('admin/', admin.site.urls),
    url('',include('instagram.urls')),
    url('accounts/register/', RegistrationView.as_view(success_url='/'),name='django_registration_register'),
    url('accounts/', include('django.contrib.auth.urls')),
    url('accounts/', include('django_registration.backends.one_step.urls')),

]
