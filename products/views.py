from django.shortcuts import render, get_object_or_404
from .models import About, Product, ProductMedia, ProductCategory,Founder, Team

# Create your views here.

def home(request):
    about = About.objects.all()
    products = Product.objects.order_by()[:4]
    founder = Founder.objects.all()
    teamindex = Team.objects.order_by()[:5] 
    return render(request,  'index.html', {'about': about, 'products': products, 'founder': founder, 'teamindex': teamindex})

def about(request):
    aboutpage = About.objects.all()
    return render(request, 'about.html', {'aboutpage': aboutpage})

def product_detail_view(request, product_slug):
    product = get_object_or_404(Product, product_slug=product_slug)
    product_images = Product.objects.all()  # Fetch related product media

    context = {
        'product': product,
        'product_images': product_images,
    }
        
    return render(request, 'products.html', context)

def product_list(request):
    p_list = Product.objects.all()
    return render(request, 'productlist.html', {'p_list': p_list})

def founder(request, fname_slug):
    founders = Founder.objects.all()
    return render(request, 'profile.html', {'founders': founders})

def team(request, tname_slug):
    team = get_object_or_404(Team, tname_slug=tname_slug)
    return render(request, 'team.html', {'team': team})

def teamlist(request):
    teamlist = Team.objects.order_by('-id')
    return render(request, 'teamlist.html', {'teamlist': teamlist})
 

    