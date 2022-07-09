from django.urls import path
from . import views
app_name = 'Account'
urlpatterns = [
    path('sign_up', views.sing_up, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),
    # path('next', views.next_sign, name='next'),
    # path('test', views.test, name='test'),
    # path('create', views.api_users, name='create'),
    path('profile', views.edit_sign, name='profile_detail')
]
