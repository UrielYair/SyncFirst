"""sync_first URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from sync_first_app import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^at_risk/', views.get_people_who_might_be_at_risk),
    url(r'^a_threat/', views.get_people_who_might_be_a_threat),
    url(r'^monitored/', views.get_events_for_monitored_person),
    url(r'^report_new/', views.get_new_incident_form),
    url(r'^incidents_by_id/', views.get_new_incident_form),
    url(r'^api/mark_event_as_viewed', views.mark_event_as_viewed),
    url(r'^api/change_person_status', views.change_person_status),
]
