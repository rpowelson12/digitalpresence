from django.shortcuts import render

# Create your views here.
def dashboard(request):
    if request.user.is_authenticated:
        first_name = request.user.first_name
        context = {'first_name': first_name}

    else:
        context = {'username': "Guest"}
    return render(request, 'dashboard/dashboard.html', context)
