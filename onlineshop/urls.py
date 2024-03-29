from django.urls import path
from . import views
from .views import ContactCreate, thanks

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout_view, name="logout"),
    path("contact/", ContactCreate.as_view(), name="contact"),
    path("thanks/", thanks, name="thanks"),
    path("cart/", views.cart, name="cart"),
    path("<str:article_title>", views.article, name="article"),
   
]