from django.conf.urls import url,include
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns=[
    url('',views.index,name='index'),
    url('account/', include('django.contrib.auth.urls')),
    url('account/', include('django.contrib.auth.urls')),
    url('profile/<str:username>/',views.profile,name='profile'),
    url('edit/profile/',views.update_profile,name='update'),
    url('image/',views.post,name='post'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)