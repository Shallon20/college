from django.shortcuts import render

from library.models import LibraryIntro, LibraryServices, LibraryStaff, LibraryContacts


# Create your views here.
def library(request):
    library_intro=LibraryIntro.objects.first()
    library_services=LibraryServices.objects.all()
    library_staff=LibraryStaff.objects.all()
    library_contacts=LibraryContacts.objects.first()
    return render(request, 'library.html', {'library_intro':library_intro, 'library_services':library_services, 'library_staff':library_staff, 'library_contacts':library_contacts })
