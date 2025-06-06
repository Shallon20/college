"""
URL configuration for DjangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path, include
from . import settings
from django.conf.urls.static import static
from myapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('office-of-dean-of-students/', views.officeOfDos, name='officeOfDos'),
    path('student-association/', views.studentAssociation, name='studentAssociation'),
    path('jobs-internships-advertisements/', views.jobsInternships, name='jobsInternships'),
    path('sports-clubs/', views.sportsClubs, name='sportsClubs'),
    path('accommodation/', views.accommodation, name='accommodation'),
    path('dispensary/', views.dispensary, name='dispensary'),
    path('cafeteria/', views.cafeteria, name='cafeteria'),
    path('upcoming-news-events/', views.upcomingNewsEvents, name='upcomingNewsEvents'),
    path('past-news-events/', views.pastNewsEvents, name='pastNewsEvents'),
    path('news-events-detail/<slug:slug>/', views.NewsEventsDetail, name='news_events_detail'),
    path('enroll/', views.enroll, name='enroll'),
    path('contact/', views.contact, name='contact'),
    path('frequently-asked-questions/', views.faq, name='faq'),
    path('library/', include('library.urls')),
    path('alumni-association/', include('alumni.urls')),
    path('search/', views.site_search, name='site_search'),
    path('admin/', admin.site.urls),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
