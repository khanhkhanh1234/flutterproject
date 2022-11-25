from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('logout', views.logout, name='logout'),
    path('nhandienbienso', views.nhandienbienso, name='nhandienbienso'),
    path('quanlykhachhang', views.quanlykhachhang, name='quanlykhachhang'),
    path('quanlygiaxe', views.quanlygiaxe, name='quanlygiaxe'),
    path('dangkyguixe', views.dangkyguixe, name='dangkyguixe'),
    path('settings', views.settings, name='settings'),
]
