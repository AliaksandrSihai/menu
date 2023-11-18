from django.urls import path
from menu.apps import MenuConfig
from menu.views import MenuListView, MenuDetailView

app_name = MenuConfig.name

urlpatterns = [
    path('', MenuListView.as_view(), name='menu_list'),
    path('menu/<int:pk>', MenuDetailView.as_view(), name='menu'),
]
