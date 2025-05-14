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
    return render(request, 'accomodation.html')


def dispensary(request):
    return render(request, 'dispensary.html')