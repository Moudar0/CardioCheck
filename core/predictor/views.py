from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import requests
import numpy as np
import pandas as pd

from predictor.forms import HeartDiseaseForm
from .models import model  # Import the loaded model  

@login_required(login_url='login')
def heart(request):
	
	
	value = ''

	if request.method == 'POST':
		# Retrieve the user input from the form
		age = float(request.POST['age'])
		sex = float(request.POST['sex'])
		cp = float(request.POST['cp'])
		trestbps = float(request.POST['trestbps'])
		chol = float(request.POST['chol'])
		fbs = float(request.POST['fbs'])
		restecg = float(request.POST['restecg'])
		thalach = float(request.POST['thalach'])
		exang = float(request.POST['exang'])
		oldpeak = float(request.POST['oldpeak'])
		slope = float(request.POST['slope'])
		ca = float(request.POST['ca'])
		thal = float(request.POST['thal'])

		# Create a numpy array with the user's data
		user_data = np.array(
			(age,
			sex,
			cp,
			trestbps,
			chol,
			fbs,
			restecg,
			thalach,
			exang,
			oldpeak,
			slope,
			ca,
			thal)
		).reshape(1, 13)

		
		predictions = model.predict(user_data) # Make predictions on the user's data

		if int(predictions[0]) == 1:
			value = 'have' # User is predicted to have heart disease
		elif int(predictions[0]) == 0:
			value = "don\'t have" # User is predicted to not have heart disease

	return render(request,
				'heart.html',
				{
					'context': value,
					'title': 'Heart Disease Prediction',
					'active': 'btn btn-success peach-gradient text-white',
					'heart': True,
					'form': HeartDiseaseForm(),
				})


def home(request):
	return render(request,
				'home.html')

def contact(request):
	return render(request,'contact.html')


# Sign Up View
def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# Login View
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('heart')  # Redirect to a restricted page, e.g., 'heart'
        else:
            messages.error(request, "Invalid username or password.")
    
    return render(request, 'registration/login.html')

# Logout View
def logout_view(request):
    logout(request)
    messages.success(request, "You have been logged out.")
    return redirect('login')


# articles
def articles(request):
  url = 'https://newsapi.org/v2/top-headlines?category=health&apiKey=4d5e6242671844fd95138d65c461147d'
  params = {
       
       
    'apiKey': '4d5e6242671844fd95138d65c461147d',  # استبدل YOUR_API_KEY بمفتاح API الخاص بك
    'language': 'en'

  }

  

  response = requests.get(url, params=params)
  data = response.json()

  # تحقق من أن الحالة 'ok' وتجنب المقالات المحذوفة
  articles_list = [
        article for article in data.get('articles', [])
        if article.get('title') and article.get('content') and
           '[Removed]' not in article['title'] and '[Removed]' not in article['content']
    ]

  context = {'articles': articles_list[:50]}  # عرض 50 مقالات فقط كبداية
  return render(request, 'articles.html', context)