from django.urls import path
from.views import home_view,list,checkout,login_view,register_view,choice
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    path('home/',home_view,name="home"),
    path('list/',list,name="list"),
    path('list/<int:id>/',checkout,name='checkout'),
    path('login/',login_view,name='login'),
    path('register/',register_view,name='register'),
    path('',choice,name='choice')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)