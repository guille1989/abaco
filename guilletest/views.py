from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views import View
from .forms import RegistrationForm
from .forms import MyTextInputForm 
from .models import TextInputs
from .models import ScrapingCounter
from .scraping import AbstractScrapingClass
import time
from django.http import HttpResponseServerError

# Create your views here.

# User log in view
class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')
    
    def post(self, request):
        #print("Aqui el post")
        username=request.POST.get('username')
        password=request.POST.get('password')
        if username == 'abacotestscraping' and password == 'TEst1234$':
            return redirect('scrape_view')
        else:
            user=authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = f'/home/?username={user}' #Set the name of the user name to be displayed in the home page
                return redirect(redirect_url) #Navigate to home page of the application
            else:
                return render(request, 'login.html', {'error': 'Invalid username or password --> data credentials.'})

# Home view of application
def home_view(request):
    # First: read if is data in database    
    # print(request.GET.get('username'))
    data = TextInputs.objects.filter(user_name=request.GET.get('username')).order_by('-created_at') # Retrive all objects in data base

    # POST handling to know if user is adding new "Maullido"
    if request.method == 'POST':    
        form = MyTextInputForm(request.POST)       
        if form.is_valid():   
            user_name = form.cleaned_data['user_name']    
            redirect_url = f'/home/?username={user_name}'           
            form.save()
            return redirect(redirect_url)
    else:
        form = MyTextInputForm()

    return render(request, 'home.html', {'form': form, 'data': data})

# User log out view
def logout_user(request):
     logout(request)
     return redirect('login')

# User registration view
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            redirect_url = f'/home/?username={username}'
            form.save()
            return redirect(redirect_url)        
    else:
        form = RegistrationForm()
    
    return render(request, 'register.html', {'form': form})

# Function to navigate to another user page and see the "Maullidos"
def other_user_texts(request):

    user = request.GET.get('user')
    query = TextInputs.objects.filter(user_name=user).order_by('-created_at') # Retrive all objects in data base
    data = list(query.values())
    
    return JsonResponse(data, safe=False)

# Scraping
def scrape_view(request):
    scraper = AbstractScrapingClass()

    try:
        data = scraper.process()
        pass
    except Exception as e:
        # handle the exception
        return render(request, 'login.html', {'error_scraping': "An error occurred in Scraping process, pleas retry !!!: {}".format(str(e))})
    
    #data = scraper.process()
    
    if data is not None:
        # Process and manipulate the scraped data
        return render(request, 'home-scraping.html', {'data': data})
    else:
        # Handle the case when the scraping fails
        return render(request, 'home-scraping.html')
    
# Scraping History
def scraping_history(request):
    data = ScrapingCounter.objects.all()

    return render(request, 'scraping.history.html', {'data': data})