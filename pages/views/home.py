from django.shortcuts import render

def home_view(request):
    context =  {
        'title': 'Home Page'
    }
    return render(request, 'pages/home.html', context)