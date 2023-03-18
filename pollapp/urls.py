from django.urls import path
from pollapp import views

app_name = 'pollapp'

urlpatterns = [
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/<poll_id>/', views.vote, name='vote'),
    path('results/<poll_id>/', views.results, name='results'),
    path('confirm-delete/<int:poll_id>/', views.confirm_delete_poll, name='confirm_delete_poll'),
    path('delete/<int:poll_id>/', views.delete_poll, name='delete_poll'),
    #  path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
]
 