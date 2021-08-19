from django.urls import path
from . import views

urlpatterns = [
    path('', views.notepads, name='notelist'),
    path('<str:title>/<int:day>/<int:month>/<int:year>/', views.note_detail, name='note_detail')
]
