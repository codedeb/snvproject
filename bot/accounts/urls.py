from django.urls import path
from.views import registrationView, logingView, homeView
urlpatterns = [
    path('', homeView, name='home'),
    path('register/', registrationView, name='register'),
    path('login/', logingView, name='login')
]
