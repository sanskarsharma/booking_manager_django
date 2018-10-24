from django.urls import path

from . import views

app_name = "booking_manager_app"
urlpatterns = [
    path('', views.app_home, name="app_home"),
    path('screen/<str:name>', views.ScreenView.as_view(), name="screen"),
    path('screens/', views.ScreenListView.as_view(), name="screens"),

]
