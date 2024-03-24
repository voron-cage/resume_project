from django.urls import path
from user_profile import views

urlpatterns = [
    path('user/register/', views.UserCreate.as_view()),
    path('user_profile/<str:username>/', views.UserProfileView.as_view()),
]
