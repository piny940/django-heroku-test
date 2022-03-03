from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index_view(request):
    html = '''
    <h1>Heroku Test!</h1>
    <p>Hello World!</p>
    '''
    return HttpResponse(html)
