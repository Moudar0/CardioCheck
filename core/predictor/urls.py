from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
  path('heart', views.heart, name="heart"),
  path('', views.home, name="home"),
  path('articles/', views.articles, name="articles"),
  path('contact',views.contact,name="contact" ),
  path('signup/', views.signup, name='signup'),
  path('login/', views.login_view, name='login'),  # Reference your custom login view here
  path('logout/', views.logout_view, name='logout'),
  # other paths
]


