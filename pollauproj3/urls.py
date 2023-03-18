

"""poll_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path

# from pollapp import views as poll_views

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', poll_views.home, name='home'),
#     path('create/', poll_views.create, name='create'),
#     path('vote/<poll_id>/', poll_views.vote, name='vote'),
#     path('results/<poll_id>/', poll_views.results, name='results'),
# ]


from django.contrib import admin
from django.urls import path
from auapp.views import uhome,usignup,ulogout,ucp
from pollapp import views 
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",uhome,name="uhome"),
    path("usignup",usignup,name="usignup"),
    # path("uwelcome",uwelcome,name="uwelcome"),
    path("ulogout",ulogout,name="ulogout"),
    path("ucp",ucp,name="ucp"),
    path('poll/', include(('pollapp.urls', 'pollapp'), namespace='poll')),
    path('home/', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('vote/<int:poll_id>/', views.vote, name='vote'),
    path('results/<int:poll_id>/', views.results, name='results'),
    path('polls/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
    path('polls/<int:poll_id>/delete/confirm/', views.confirm_delete_poll, name='confirm_delete_poll'),
    # path('poll/<int:poll_id>/delete/', views.delete_poll, name='delete_poll'),
]

handler404="auapp.views.pnf"
handler500="auapp.views.server_error"