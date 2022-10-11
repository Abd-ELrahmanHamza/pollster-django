from django.shortcuts import render


def index(request):
    print("here")
    return render(request, 'pages/index.html')
