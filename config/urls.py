"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from myuser.views import login_view, logout_view
from bugtracker.views import change_status, edit_ticket_view, home_view, invalid_ticket, ticket_view, add_ticket_view, user_view
urlpatterns = [
    path('', home_view, name='home'),
    path('ticket/<int:ticket_id>/', ticket_view, name='ticket view'),
    path('edit/<int:ticket_id>/', edit_ticket_view, name='edit ticket'),
    path('status/<int:ticket_id>/', change_status),
    path('invalid/<int:ticket_id>/', invalid_ticket),
    path('user/<int:user_id>/', user_view, name='user view'),
    path('addticket/', add_ticket_view, name='add ticket'),
    path('login/', login_view),
    path('logout/', logout_view),
    path('admin/', admin.site.urls),
]
