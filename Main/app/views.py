"""
Definition of views.
"""

from django.shortcuts import render
from app import views
import app
from django.http import HttpRequest
from django.http import HttpResponseRedirect
from django.template import RequestContext
from datetime import datetime

#import the module with the function to be executed
from app.management.commands.TestButton import func
from app.management.commands.operations import grayscale

#function used to run the test python script
def runButton(request):
    func()
    return HttpResponseRedirect('/')

#function used for grayscale operation
def operations(request):
    grayscale()
    return HttpResponseRedirect('/')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }


    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Abagiu Marian',
            'year':datetime.now().year,
        }
    )


def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Image Processing Toolbox',
            'year':datetime.now().year,
        }
    )


