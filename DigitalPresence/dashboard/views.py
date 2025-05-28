from django.http import HttpResponse
from django.shortcuts import redirect, render
import tweepy, os
from dotenv import load_dotenv

# Create your views here.

load_dotenv()

def dashboard(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        context = {'first_name': first_name}

    else:
        context = {'username': "Guest"}
    return render(request, 'dashboard/dashboard.html', context)

def twitter(request):
    
    return render(request, 'dashboard/twitter.html')

def twitter_login(request):
    oauth2_user_handler = create_oauth_handler_initial()
    authUrl = oauth2_user_handler.get_authorization_url()
    context ={
        'authUrl': authUrl,
    }
    print("Twitter Auth URL:", authUrl)

    request.session['code_verifier'] = oauth2_user_handler._client.code_verifier

    return redirect(authUrl)

def twitter_success(request):
    oauth2_user_handler = create_oauth_handler_with_verifier(request)
    authorization_response = request.build_absolute_uri()
    token = oauth2_user_handler.fetch_token(authorization_response)

    print("Access token:", token)

    return render(request, 'dashboard/twitter_success.html')

def create_oauth_handler_initial():
    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id=os.getenv("CLIENT_ID"),
        redirect_uri="http://127.0.0.1:8000/twitter/success",
        scope=['offline.access', 'tweet.write'],
        client_secret=os.getenv("CLIENT_SECRET"),
    )
    return oauth2_user_handler

def create_oauth_handler_with_verifier(request):
    code_verifier = request.session.get('code_verifier')
    if not code_verifier:
        raise Exception("Missing code_verifier in session")

    oauth2_user_handler = tweepy.OAuth2UserHandler(
        client_id=os.getenv("CLIENT_ID"),
        redirect_uri="http://127.0.0.1:8000/twitter/success",
        scope=['offline.access', 'tweet.write'],
        client_secret=os.getenv("CLIENT_SECRET"),
    )

    oauth2_user_handler._client.code_verifier = code_verifier

    return oauth2_user_handler