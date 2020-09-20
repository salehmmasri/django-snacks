from .views import HomeView, AboutView
from django.urls import path

urlpatterns = [
    path('', HomeView.as_view(), name='drink-home'), # Step 3: Adding home url using HomeView
    path('prodacts', AboutView.as_view(), name='products'),
]