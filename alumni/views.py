from django.shortcuts import render, redirect

from alumni.forms import AlumniMessageForm
from alumni.models import Alumni, WhyStayConnected, AlumniBoard, AlumniContacts


# Create your views here.
def alumni(request):
    alumni_contacts=AlumniContacts.objects.first()
    alumni_intro=Alumni.objects.first()
    why_stay_connected=WhyStayConnected.objects.all()
    alumni_board=AlumniBoard.objects.all()
    form = AlumniMessageForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        return redirect('alumni')
    return render(request, 'alumni.html', {'alumni_intro':alumni_intro, 'form':form, 'why_stay_connected':why_stay_connected, 'alumni_board':alumni_board, 'alumni_contacts':alumni_contacts})
