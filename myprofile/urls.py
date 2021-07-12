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
    url('search/', views.search_profile, name='search'),
    url('user_profile/<username>/', views.user_profile, name='user_profile'),
    # url('unfollow/<to_unfollow>', views.unfollow, name='unfollow'),
    # url('follow/<to_follow>', views.follow, name='follow'),
    # url('image/<id>', views.comment, name='comment'),
    

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)