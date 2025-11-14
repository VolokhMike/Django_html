from django.urls import path

from . import views

urlpatterns = [
    path("", views.product_list, name="product_list"),
    path("<int:product_pk>/<slug:product_slug>/", views.product_detail,name="product_detail",),
]
