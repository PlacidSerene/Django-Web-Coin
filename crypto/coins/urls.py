from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login',views.login_view, name='login'),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('users/<int:user_id>/buying', views.buying, name='buying'),
    path('users/<int:user_id>/selling', views.buying, name='selling'),
    path('users/<int:user_id>/asset', views.asset, name='asset'),
    path('test', views.test, name='asset'),
    path('landing', views.landing, name='landing')
]