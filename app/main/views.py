import os

from flask import render_template,request, redirect, url_for, abort
from . import main
from .forms import PostForm
from ..models import Post
from .. import db
from app.requests import getQuotes
from flask_login import login_required

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    quotes=getQuotes()
    posts = Post.query.all()
    title='Quotes Blog'
    return render_template('index.html',title=title,quotes=quotes,posts=posts)



@main.route("/new_post", methods=['GET', 'POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post(title=form.title.data, content=form.content.data)
        post.save()
        flash('Your post has been created!', 'success')
        return redirect(url_for('main.index'))
    return render_template('new_post.html', title='New Post',
                           form=form, legend='New Post')