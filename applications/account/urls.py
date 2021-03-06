from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.RegisterView.as_view()),
    path('activate/<str:activation_code>/', views.ActivationView.as_view()),
    path('login/', views.LoginView.as_view()),
    path('logout/', views.LogoutView.as_view()),
    path('profile/', views.ProfileView.as_view()),
    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view()),
    path('password-reset/', include('django_rest_passwordreset.urls')),
]
