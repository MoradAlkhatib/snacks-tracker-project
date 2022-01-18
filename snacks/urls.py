from django.urls import path
from .views import HomeView ,SnackListDetail

urlpatterns = [
    path('', HomeView.as_view() , name = 'home' ),
    path('<int:pk>/',SnackListDetail.as_view(),name = 'list_detail')
]