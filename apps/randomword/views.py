from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string
import random
import string


def random_word(n):
    return get_random_string(length=14)

def index(request):
    try:
        request.session['tries']
    except KeyError:
        request.session['tries'] = 0
    return render(request, "randomword/index.html" )

def generate(request):
    request.session['tries'] += 1
    request.session['word'] = random_word(14)
    return redirect('/')

def reset(request):
    del request.session['tries']
    del request.session['word']
    return redirect ('/')
