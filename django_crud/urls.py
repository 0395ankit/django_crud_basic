from django.urls import path
from .views import CartItemViews

urlpatterns = [
    path('cart/', CartItemViews.as_view()),
    path('cart/<int:id>', CartItemViews.as_view())
]
