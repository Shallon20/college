from django.shortcuts import render, redirect, get_object_or_404
from myapp.forms import HostelApplicationForm, EnrollmentForm, ContactUsForm
from myapp.models import CarouselSlide, NewsEvents, Faculty, GalleryImage, Testimonial, AboutInfo, WhyChooseUs, Stats, \
    VisionMission, StaffMember, DeanProfile, DeanStaff, StudentLeadership, JobsInternshipsAds, Sport, Club, Hostel, \
    DispensaryService, DispensaryContact, DispensaryGallery, CafeteriaImage, CafeteriaService, CafeteriaMenu, \
    CafeteriaMenuPDF, ContactInfo


# Create your views here.
def home(request):
    slides = CarouselSlide.objects.all()
    news_events = NewsEvents.objects.filter(is_new=True).order_by('-date')[:4]
    faculties = Faculty.objects.all()
    gallery_images = GalleryImage.objects.all()[:9]
    testimonials = Testimonial.objects.all()[:4]

    context = {
        'slides': slides,
        'news_events': news_events,
        'faculties': faculties,
        'gallery': gallery_images,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)


def about(request):
    about_info = AboutInfo.objects.all()
    why_choose_us = WhyChooseUs.objects.all()
    stats = Stats.objects.all()
    vision_mission = VisionMission.objects.all()
    staffs = StaffMember.objects.all()
    context = {
        'about_info': about_info,
        'why_choose_us': why_choose_us,
        'stats': stats,
        'vision_mission': vision_mission,
        'staffs': staffs,
    }
    return render(request, 'about.html', context)


def courses(request):
    faculties = Faculty.objects.prefetch_related('courses').all()
    return render(request, 'courses.html', {'faculties': faculties})


def officeOfDos(request):
    dean = DeanProfile.objects.first()
    staffs = DeanStaff.objects.all()
    return render(request, 'dos.html', {'dean': dean, 'staffs': staffs})


def studentAssociation(request):
    student_leadership = StudentLeadership.objects.all()
    return render(request, 'students-association.html', {'student_leadership': student_leadership})


def jobsInternships(request):
    jobs_internships_ads = JobsInternshipsAds.objects.all()
    return render(request, 'jobs-internships.html', {'jobs_internships_ads': jobs_internships_ads})


def sportsClubs(request):
    sports = Sport.objects.prefetch_related('images').all()
    clubs = Club.objects.prefetch_related('images').all()
    return render(request, 'sports-clubs.html', {'sports': sports, 'clubs': clubs})

def accommodation(request):
    hostels = Hostel.objects.prefetch_related('images').all()
    if request.method == 'POST':
        form = HostelApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            form = HostelApplicationForm()
    else:
        form = HostelApplicationForm()
    return render(request, 'accommodation.html', {'hostels': hostels, 'form': form})

def dispensary(request):
    services = DispensaryService.objects.all()
    contacts = DispensaryContact.objects.filter(is_active=True).first()
    images = DispensaryGallery.objects.all()
    return render(request, 'dispensary.html', {'services': services, 'contacts': contacts, 'images': images})

def cafeteria(request):
    cafeteria_images = CafeteriaImage.objects.all()
    cafeteria_services = CafeteriaService.objects.first()
    cafeteria_menu = CafeteriaMenu.objects.all()
    pdf = CafeteriaMenuPDF.objects.last()

    context = {
        'cafeteria_images': cafeteria_images,
        'cafeteria_services': cafeteria_services,
        'cafeteria_menu': cafeteria_menu,
        'pdf': pdf,
    }
    return render(request, 'cafeteria.html', context)

def upcomingNewsEvents(request):
    news_events = NewsEvents.objects.filter(is_new=True).order_by('-date')
    return render(request, 'upcoming-events.html', {'news_events': news_events})


def pastNewsEvents(request):
    news_events = NewsEvents.objects.filter(is_new=False).order_by('-date')
    return render(request, 'past-events.html', {'news_events': news_events})


def NewsEventsDetail(request, slug):
    news_events = get_object_or_404(NewsEvents, slug=slug)
    return render(request, 'event-detail.html', {'slug': slug, 'news_events': news_events})


def enroll(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid:
            return redirect('home')
    else:
        form = EnrollmentForm()
    return render(request, 'enroll.html', {'form': form})


def contact(request):
    contact_info = ContactInfo.objects.all()
    if request.method == 'POST':
        form = ContactUsForm(request.POST)
        if form.is_valid:
            return redirect('home')
    else:
        form = ContactUsForm()
    return render(request, 'contact.html', {'form': form, 'contact_info': contact_info})


def faq(request):
    return render(request, 'faq.html')

def library(request):
    return render(request, 'library.html')
