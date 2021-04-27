from django.urls import path
from . import views

urlpatterns = [
    path("",views.canvas,name="canvas"),
    path('savecanvas',views.savecanvas,name='savecanvas'),
]