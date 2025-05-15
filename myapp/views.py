from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')


def courses(request):
    return render(request, 'courses.html')


def officeOfDos(request):
    return render(request, 'dos.html')


def studentAssociation(request):
    return render(request,'students-association.html')


def jobsInterniships(request):
    return render(request, 'jobs-internships.html')


def sportsClubs(request):
    return render(request, 'sports-clubs.html')


def accommodation(request):
    return render(request, 'accommodation.html')


def dispensary(request):
    return render(request, 'dispensary.html')


def cafeteria(request):
    return render(request, 'cafeteria.html')


def upcomingNewsEvents(request):
    return render(request, 'upcoming-events.html')


def pastNewsEvents(request):
    return render(request, 'past-events.html')


def NewsEventsDetail(request, slug):
    return render(request, 'event-detail.html', {'slug': slug})

def enroll(request):
    return render(request, 'enroll.html')


def contact(request):
    return render(request, 'contact.html')


def faq(request):
    return render(request, 'faq.html')


def alumni(request):
    return render(request, 'alumni.html')


def library(request):
    return render(request, 'library.html')