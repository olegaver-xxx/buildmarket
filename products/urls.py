from django.urls import path
from . import views
urlpatterns = [
    path('', views.product, name="product"),
    path('<int:product_id>/', views.product_id, name="product_id"),
]
