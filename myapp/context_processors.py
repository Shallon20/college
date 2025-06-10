from .models import Logo, SocialLinks

def logo_details(request):
  logo = Logo.objects.first()
  return {'logo': logo}

def social_links(request):
    social_links = SocialLinks.objects.all()
    return {'social_links': social_links}