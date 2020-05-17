from django.urls import path, include
from . import views

urlpatterns = [
        path('', views.note_form,          name='note_insert'),
        path('<int:id>/', views.note_form, name='note_update'),
        path('list/', views.note_list,     name='note_list'),
        path('delete/<int:id>/', views.note_delete, name='note_delete')
        ]
