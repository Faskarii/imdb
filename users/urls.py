from django.urls import path
from .views import user_login, user_sign_up, user_view

urlpatterns = [
    path('login/', user_login, name='login'),
    path('signup/', user_sign_up, name='sign_up'),
    path('panel/', user_view, name='profile'),
]
