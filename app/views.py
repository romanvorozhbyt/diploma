from django.shortcuts import render

# Create your views here.
def user_search(request):
    return render(request, 'app/userSearch.html', {})