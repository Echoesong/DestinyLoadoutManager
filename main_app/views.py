from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
#Oauth 2.0 stuff:
from django.http import HttpResponseRedirect
from django.conf import settings
import uuid
import requests
from django.http import JsonResponse

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('home')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)

def bungie_auth(request):
  state = uuid.uuid4()
  request.session['bungie_auth_state'] = str(state)
  auth_url = f"{settings.BUNGIE_AUTHORIZATION_URL}?client_id={settings.BUNGIE_CLIENT_ID}&response_type=code&state={state}"
  return HttpResponseRedirect(auth_url)

def bungie_callback(request):
    code = request.GET.get('code')
    state = request.GET.get('state')
    stored_state = request.session.get('bungie_auth_state')

    if state != stored_state:
        return JsonResponse({"error": "Invalid state parameter"})

    data = {
        "grant_type": "authorization_code",
        "code": code,
        "client_id": settings.BUNGIE_CLIENT_ID,
        "client_secret": settings.BUNGIE_CLIENT_SECRET
    }
    response = requests.post(settings.BUNGIE_TOKEN_URL, data=data)
    token_data = response.json()

# 
    return JsonResponse(token_data)

