from flask import render_template,request,redirect,url_for
from . import main


@main.route('/')
def index():
    '''
    View root page function that returns the source page and some data
    '''

    
    title = 'Home - Welcome to The best pitches resource online'
    return render_template('index.html', title = title )