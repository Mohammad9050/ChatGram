from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'Chats'
urlpatterns = [
    path('add/<int:num>', views.add_friend, name='add'),
    path('remove/<int:num>', views.remove_friend, name='remove'),
    path('chat_box/<int:num>', views.text_box_view, name='chat_box'),
    path('test2',TemplateView.as_view(template_name='Chats/pro_test2.html')),
    path('', views.test_view, name='test'),
    path('box', views.friend_box, name='box'),

]
