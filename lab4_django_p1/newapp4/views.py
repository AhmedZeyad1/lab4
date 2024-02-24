from django.shortcuts import render

def default_view(request):
    "The view for the default path"
    return render(request, 'tax/default.html')


