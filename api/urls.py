from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('line', views.line, name="line"),
    path('api/clova', views.clova),
    path('api/clova/status', views.status),
]
