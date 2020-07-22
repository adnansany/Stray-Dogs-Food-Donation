from django.urls import path
from .import views

urlpatterns = [
    path('',views.HomeView.as_view(),name="home"),
    path('login/',views.LoginViews.as_view(),name="login"),
    path('signin/',views.SigninViews.as_view(),name="signin"),

]