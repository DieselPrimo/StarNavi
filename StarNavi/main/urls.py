from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'^signup/', views.signup),
    url(r'^login/', views.login),
    url(r'^create_post/', views.create_post),
    url(r'^like/', views.like),
    url(r'^unlike/', views.unlike),
]
