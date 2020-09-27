import os

from flask import render_template,request,redirect,url_for
from . import main
from app.requests import getQuotes
# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes=getQuotes()
    title='Quotes Blog'
    return render_template('index.html',title=title,quotes=quotes)