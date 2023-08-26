from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
# Create your views here.
def home(request):
    queryset = movie.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    
    return render(request,'home.html',context = {'movies' : queryset, 'page' : 'home'})

def about(request):
    context = { 'page' : 'about' }
    return render(request,'about.html',context)

def contact(request):
    context = { 'page' : 'contact' }
    return render(request,'contact.html',context)

def readdata(request):
    if request.method=="POST":
        data = request.POST

        name = data.get('name')
        rdate = data.get('release_date')
        dir = data.get('director')
        sum = data.get('summary')
        img = request.FILES.get('image')

        movie.objects.create(
            name = name,
            release_date = rdate,
            director = dir,
            summary = sum,
            image = img,
        )
        return redirect('/readdata/')
    queryset = movie.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    context = { 'movies' : queryset,'page':'host'}
    return render(request, 'readdata.html',context)

def delete_movie(request ,id):
    queryset = movie.objects.get(id = id)
    queryset.delete()
    return redirect('/readdata/')

def update_movie(request,id):
    return redirect('/readdata/')

def re_front(request):
    queryset = movie.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(name__icontains = request.GET.get('search'))
    return render(request,'re_front.html',{'page':'review','movies':queryset})

def reviews(request,id):
    queryset = movie.objects.get(id = id)
    context = {'movie':queryset ,'page':'review_page'}
    if request.method == 'POST':
        _review = request.POST.get('_review')
        rating = request.POST.get('rating')
        user = request.user
        
        review.objects.create(
            user = user,
            movie_name = queryset.name,
            _review = _review,
            rating = rating,
        )
        
        average_rating = review.objects.filter(movie_name = queryset.name).aggregate(Avg('rating'))['rating__avg']
        print(average_rating,id)
        if average_rating is not None:
            Movie = movie.objects.get(id=id)
            Movie.average_rating = average_rating
            Movie.save()
        messages.info(request,'review is uploaded')
    return render(request,'reviews.html',context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if not User.objects.filter(username = username).exists():
            messages.info(request,'Invalid username')
            return redirect('/login/')
        user = authenticate(username=username , password=password)
        if user is None:
            messages.info(request,'Invalid password')
            return redirect('/login/')
        else:
            login(request,user)
            return redirect('/home/')
    return render(request,'login_page.html')

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
       
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request, "username already exist") 
            return redirect('/register/')
        user = User.objects.create(
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request, "account successfully created")
        return redirect('/register/')
    return render(request,'register.html')

def top_rated_page(request):
    sorted_queryset = movie.objects.all().order_by('-average_rating')
    return render(request,'top_rated.html',{'movies':sorted_queryset,'page':'top_rated'})